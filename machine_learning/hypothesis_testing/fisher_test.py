import numpy as np
import scipy as sp
import scipy.special as special
import scipy.stats as stats
import pandas as pd
import holoviews as hv


def fisher_exact_test(df, label, col_c, col_t):
    columns = [col_c, col_t]

    row_sums = df[columns].sum()
    sum_c = row_sums[col_c]
    sum_t = row_sums[col_t]
    xs = df[df[label] == 1]
    x_c = xs[col_c][0]
    x_t = xs[col_t][0]
    x = x_c + x_t

    factor1 = special.comb(sum_c, x_c)
    factor2 = special.comb(sum_t, x_t)
    denominator = special.comb(sum_c + sum_t, x)
    pvalue = factor1 * factor2 / denominator
    return pvalue


def gen_data(xc=12, xt=7, totalc=15, totalt=15):
    """gen_data
    Generate 2x2 contingency table

    :param xc:
    :param xt:
    :param totalc:
    :param totalt:
    """
    data = {
        'infection': [1, 0],
        'control': [xc, totalc - xc],
        'treatment': [xt, totalt - xt],
    }
    return pd.DataFrame(data=data)


def fisher_exact_test_scipy(df, label, col_c, col_t):
    columns = [col_c, col_t]

    xs = df[columns].values

    # pvalue = stats.fisher_exact(xs)
    # pvalue = stats.fisher_exact(xs, 'less')
    pvalue = stats.fisher_exact(xs, 'greater')
    return pvalue


def fisher_exact_test_scipy_mine(df, label, col_c, col_t):
    xs = df[df[label] == 1]
    x_t = xs[col_t][0]
    # N, n, K
    M, N, n = _get_M_N_n(df, label, col_c, col_t)
    pvalue = stats.hypergeom.cdf(x_t, M, n, N)
    return pvalue


def fisher_exact_test_k_alpha(df, label, col_c, col_t, alpha):
    # N, n, K
    M, N, n = _get_M_N_n(df, label, col_c, col_t)
    print('M, N, n: {0}, {1}, {2}'.format(M, N, n))
    k_alpha = N
    for i in range(N + 1):
        pvalue = stats.hypergeom.cdf(i, M, n, N)
        if pvalue < alpha:
            k_alpha = i
    print('k_alpha: {0}'.format(k_alpha))
    return k_alpha


def _get_M_N_n(df, label, col_c, col_t):
    columns = [col_c, col_t]

    row_sums = df[columns].sum()
    sum_c = row_sums[col_c]
    sum_t = row_sums[col_t]
    xs = df[df[label] == 1]
    x_c = xs[col_c][0]
    x_t = xs[col_t][0]

    # N
    M = sum_c + sum_t
    # n
    N = sum_t
    # K
    n = x_c + x_t
    return M, N, n


def wald_statistics(df, label, col_c, col_t):
    columns = [col_c, col_t]

    row_sums = df[columns].sum()
    sum_c = row_sums[col_c]
    sum_t = row_sums[col_t]
    pis = (df[df[label] == 1] / row_sums).loc[:, columns]
    pi_c = pis[col_c][0]
    pi_t = pis[col_t][0]
    x_c = pi_c * sum_c
    x_t = pi_t * sum_t
    pi = (x_c + x_t) / (sum_c + sum_t)
    print('pi: {0}'.format(pi))
    pi_c = x_c / sum_c
    pi_t = x_t / sum_t
    print('pi_c: {0}'.format(pi_c))
    print('pi_t: {0}'.format(pi_t))
    denominator = np.sqrt(pi_c * (1.0 - pi_c) / sum_c + pi_t * (1.0 - pi_t) / sum_t)
    numerator = (pi_c - pi_t)
    print('denominator: {0}'.format(denominator))
    print('numerator: {0}'.format(numerator))
    print('numerator / denominator: {0}'.format(numerator / denominator))
    return denominator / numerator


def score_statistics(df, label, col_c, col_t):
    columns = [col_c, col_t]

    row_sums = df[columns].sum()
    sum_c = row_sums[col_c]
    sum_t = row_sums[col_t]
    pis = (df[df[label] == 1] / row_sums).loc[:, columns]
    pi_c = pis[col_c][0]
    pi_t = pis[col_t][0]
    x_c = pi_c * sum_c
    x_t = pi_t * sum_t
    pi = (x_c + x_t) / (sum_c + sum_t)
    pi_c = x_c / sum_c
    pi_t = x_t / sum_t
    denominator = np.sqrt(pi * (1.0 - pi) * (1.0 / sum_c + 1.0 / sum_t))
    numerator = (pi_c - pi_t)
    return numerator / denominator


def barnard_test_pdf(df, label, col_c, col_t, pi):
    columns = [col_c, col_t]

    row_sums = df[columns].sum()
    sum_c = row_sums[col_c]
    sum_t = row_sums[col_t]
    pis = (df[df[label] == 1] / row_sums).loc[:, columns]
    pi_c = pis[col_c][0]
    pi_t = pis[col_t][0]
    x_c = pi_c * sum_c
    x_t = pi_t * sum_t

    factor_c = special.comb(sum_c, x_c)
    factor_t = special.comb(sum_t, x_t)
    factor1 = pi ** (x_c + x_t)
    factor2 = (1.0 - pi) ** (sum_c + sum_t - x_c - x_t)
    pdf = factor_c * factor_t * factor1 * factor2
    return pdf


def barnard_test(df, label, col_c, col_t, pi):
    columns = [col_c, col_t]
    row_sums = df[columns].sum()
    sum_c = row_sums[col_c]
    sum_t = row_sums[col_t]

    statistics = score_statistics(df, label, col_c, col_t)
    # if you want to reproduce the result of
    # Mehta, C. R., & Senchaudhuri, P. (2003). Conditional versus Unconditional Exact Tests for Comparing Two Binomials.
    # statistics = round(statistics, 3)
    summand = 0.0
    for xc in range(sum_c + 1):
        for xt in range(sum_t + 1):
            df_new = gen_data(xc=xc, xt=xt)
            statistics_new = score_statistics(df_new, label, col_c, col_t)
            # statistics_new = round(statistics_new, 3)
            if statistics <= statistics_new:
                summand += barnard_test_pdf(df_new, label, col_c, col_t, pi)

    return summand


def barnard_test_pvalue(df, label, col_c, col_t):
    # TODO
    # compute sup{barnard_test(pi) | pi in (0, 1)}
    pass


def draw_barnard_test(df, label, col_c, col_t, columns):
    xs = [0.1 * x for x in range(10)]
    ys = [barnard_test(df, 'infection', columns[0], columns[1], x) for x in xs]
    return hv.Curve((xs, ys), label='label')


def run_fisher_test():
    df = gen_data()
    columns = ['control', 'treatment']
    fet_pvalue = fisher_exact_test(df, 'infection', columns[0], columns[1])
    print('fisher_exact_test pvalue: {0}'.format(fet_pvalue))
    fets_pvalue = fisher_exact_test_scipy(df, 'infection', columns[0], columns[1])
    print('fisher_exact_test scipy_pvalue: {0}'.format(fets_pvalue))
    fetsm_pvalue = fisher_exact_test_scipy_mine(df, 'infection', columns[0], columns[1])
    print('fisher_exact_test scipy_mine_pvalue: {0}'.format(fetsm_pvalue))
    # fisher_exact_test_k_alpha(df, 'infection', columns[0], columns[1], 0.05)


def run_barnard_test():
    df = gen_data()
    columns = ['control', 'treatment']
    # wald_statistics(df, 'infection', columns[0], columns[1])
    # ss = score_statistics(df, 'infection', columns[0], columns[1])
    # expect 0.026551737528245266
    bt = barnard_test(df, 'infection', columns[0], columns[1], 0.3365)
    print(bt)
    draw_barnard_test(df, 'infection', columns[0], columns[1], columns)


run_fisher_test()
run_barnard_test()

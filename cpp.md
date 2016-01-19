# C++

## template

### templateクラスの型推論
```cpp
template <typename E>
class test {

};

template <typename E>
class base {

};

class derived : public base <derived> {

};

template <typename E>
struct traits {
    static void apply() {
        std::cout << "traits<E>" << std::endl;
    }
};

template <typename E>
struct traits<test<E> > {
    static void apply() {
        std::cout << "traits<test<E> >" << std::endl;
    }
};

template <typename E>
struct traits<base<E> > {
    static void apply() {
        std::cout << "traits<base<E> >" << std::endl;
    }
};

int main(int argc, char const* argv[])
{
    traits<double>::apply();
    traits<test<double> >::apply();
    traits<test<base<test<double> > > >::apply();
    traits<base<derived> >::apply();
    traits<derived>::apply();
    traits<test< base<derived> > >::apply();
    traits<base<test<double> > >::apply();
    /*
    output here
    traits<E>
    traits<test<E> >
    traits<test<E> >
    traits<base<E> >
    traits<E>
    traits<test<E> >
    traits<base<E> >
    */
    return 0;
}
```
型推論時に型の継承関係は考慮されない。
```cpp
template <typename E>
class base {

};

class derived : public base <derived> {

};

template <typename E>
struct traits {
    static void apply() {
        std::cout << "traits<E>" << std::endl;
    }
};

template <typename E>
struct traits<base<E> > {
    static void apply() {
        std::cout << "traits<base<E> >" << std::endl;
    }
};

int main(int argc, char const* argv[])
{
    traits<derived>::apply();
    /*
    output here
    traits<E>
    */
    return 0;
}

```


## typedef
### 配列のtypedef

```cpp
//int[2]のtypedef
typedef int type[2];
```
### typedefのprivate, public

```cpp
class A {
private:
    typedef int private_type;
public:
    typedef int public_type;
};

void main() {
    //A::private_type hoge; //error
    A::public_type hoge;
}
```

### typedefの継承
```cpp
class base {
public:
    typedef int type1[1];
    typedef int type2[1];
public:
    static int apply1()
    {
        return sizeof(type1);
    }
    static int apply2()
    {
        return sizeof(type2);
    }
};

class derived {
public:
    typedef int type2[2];
public:
    static int apply1()
    {
        return sizeof(type1);
    }
    static int apply2()
    {
        return sizeof(type2);
    }
};

void main()
{
    std::cout << base::apply1() << std::endl; //4
    std::cout << derived::apply1() << std::endl; //8
    std::cout << base::apply2() << std::endl; //4
    std::cout << derived::apply2() << std::endl; //4
}

```


## tips
### case1: CRTPのインスタンス化の順序
CRTPでtypedefするときの注意。
下記はderivedのtypedefされる前にbaseのtypedefが評価されるが、このときderivedのtypedefは評価されていないのでエラー。
```cpp
template <typename T>
struct base {
    typedef typename T::value_type value_type;
    static const T& operator()()
    {
        return static_cast<const T&>(*this);
    }
};

struct derived : base<derived> {
    typedef double value_type;
};
```


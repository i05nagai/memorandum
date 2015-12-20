# Visual Studio

## Viisual Studio 2015
### CppUnitを用いたTDDの環境構築 with Eclipse
以下を構築。
* targetのプロジェクトとtarget_testプロジェクトを作る。
* targetプロジェクトはdll作成
* target_testはCppUnitによる単体テストのプロジェクト
* またGMockでMockが追加できる環境を構築

1. 新規プロジェクトの作成
    * プロジェクト名:target
    * ソリューション名:sample
2. プロジェクトの設定
    * DLLの作成にチェック
    * 空のプロジェクトにチェック
3. APIファイルの追加
    // target.h
    #ifdef MATHFUNCSDLL_EXPORTS
    #define MATHFUNCSDLL_API __declspec(dllexport) 
    #else
    #define MATHFUNCSDLL_API __declspec(dllimport) 
    #endif
4. Dummyクラスの追加
    //for cpp
    
4. target_testプロジェクトを追加
    * プロジェクト名:target_test
    * コンソールアプリケーション
    * 空のプロジェクト
5. target_testにmainを追加
    
6. target_testにDummyTestクラスを追加

7. targetプロジェクトのプロパティから以下を設定。
    * Debug/Release
        * C/C++->全般->追加のインクルードディレクトリにboostのパスを設定。
        * C/C++->コマンドライン->追加のオプションに以下を追加。
        /D MC_EXPORTS
    * Debug
        * 
    * Release
8. target_testプロジェクトのプロパティから以下を設定
    * Debug/Release
        * C/C++->全般->追加のインクルードディレクトリにboost, CppUnit, GmockTestのパスを設定。
    * Debug
        * リンカー->入力->追加の依存ファイルに以下を追加
        cppunitd.lib
        cppunitd_dll.lib
        target.lib
        *リンカー->全般->追加のライブラリ依存関係のリンクに以下を追加
            * CppUnitのlib
            * GMockのlib
    * Release

### Eclipse
1. New->C++ Project
    * Project Nameを既存のVisual Studioのproject名
    * Locationはvcprojが作られるディレクトリ
    * Project Typeは,Empty Project
    * ToolChainsはMicrosfot Visual C++
2. Configurations
    * Releaseのチェックを外す（Eclipseでbuildしないので設定ファイルを一つに統一する）
3. Project->Buld Automaticallyのチェックを外す。
4. Property->C/C++ Buld->Settings->C++ Comiper->Preprocessor->Include Path
    * 必要なパスを追加




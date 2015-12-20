# CppUnit

## VisualStudio2015
### cppunit
* Debug/Release
    * 全般->構成の種類->スタティックライブラリ
* Debug
    * C/C++->コード生成->ランタイムライブラリ->マルチスレッドデバッグ
    * 全般->ターゲット名->$(ProjectName)d
* Relase
    * C/C++->コード生成->ランタイムライブラリ->マルチスレッド
### cppunit_dll
* Debug/Release
    * 全般->構成の種類->ダイナミックライブラリ
* Debug
    * C/C++->コード生成->ランタイムライブラリ->マルチスレッドデバッグDll
    * 全般->ターゲット名->$(ProjectName)d
* Relase
    * C/C++->コード生成->ランタイムライブラリ->マルチスレッドDll


@echo off
rem nkfで文字コードをUTF-8に変換する

set nkf=""
for %%V in (nkf.exe) do set nkf=%%~$PATH:V
if not "%nkf%" == "" goto start
set nkf=.\nkf.exe
if exist %nkf% goto start
echo nkf.exeが見つからないため、処理を中止します。
pause

goto end


:start
if "%~1" == "" goto noopt


:opt
rem 引数があれば指定されたファイルすべてを処理

echo 指定されたTeX関連ファイルの文字コードをUTF-8に変換します。
echo 実行しない場合は Ctrl+C を押して中止してください。
pause

:loop
if not exist "%~1" goto optsft
if exist "%~1\\" goto optsft

if "%~x1" == "" goto optsft

if %~x1 == .tex goto nkfdo
if %~x1 == .ltx goto nkfdo
if %~x1 == .aux goto nkfdo
if %~x1 == .toc goto nkfdo
if %~x1 == .lot goto nkfdo
if %~x1 == .lof goto nkfdo
if %~x1 == .idx goto nkfdo
if %~x1 == .ind goto nkfdo
if %~x1 == .bib goto nkfdo
if %~x1 == .dtx goto nkfdo
if %~x1 == .sty goto nkfdo
if %~x1 == .ist goto nkfdo
if %~x1 == .bst goto nkfdo
if %~x1 == .bbl goto nkfdo
goto optsft

:nkfdo
%nkf% -w --overwrite "%~1"

:optsft
shift
if not "%~1" == "" goto loop

goto end


:noopt
rem 引数指定がない場合

echo このフォルダ内のTeX関連ファイルの文字コードをUTF-8に変換します。
echo 実行しない場合は Ctrl+C を押して中止してください。
pause

for %%f in (*.tex, *.ltx, *.aux, *.toc, *.lot, *.lof, *.idx, *.ind, *.bib, *.dtx, *.sty, *.ist, *.bst, *.bbl) do %nkf% -w --overwrite %%f

goto end


:end
echo 終了しました。

@echo off
rem nkf�ŕ����R�[�h��UTF-8�ɕϊ�����

set nkf=""
for %%V in (nkf.exe) do set nkf=%%~$PATH:V
if not "%nkf%" == "" goto start
set nkf=.\nkf.exe
if exist %nkf% goto start
echo nkf.exe��������Ȃ����߁A�����𒆎~���܂��B
pause

goto end


:start
if "%~1" == "" goto noopt


:opt
rem ����������Ύw�肳�ꂽ�t�@�C�����ׂĂ�����

echo �w�肳�ꂽTeX�֘A�t�@�C���̕����R�[�h��UTF-8�ɕϊ����܂��B
echo ���s���Ȃ��ꍇ�� Ctrl+C �������Ē��~���Ă��������B
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
rem �����w�肪�Ȃ��ꍇ

echo ���̃t�H���_����TeX�֘A�t�@�C���̕����R�[�h��UTF-8�ɕϊ����܂��B
echo ���s���Ȃ��ꍇ�� Ctrl+C �������Ē��~���Ă��������B
pause

for %%f in (*.tex, *.ltx, *.aux, *.toc, *.lot, *.lof, *.idx, *.ind, *.bib, *.dtx, *.sty, *.ist, *.bst, *.bbl) do %nkf% -w --overwrite %%f

goto end


:end
echo �I�����܂����B

# 概要
Wikiの機能を有するWebアプリである．
マークダウンによる入力と各ページのスラッグ（URLの末尾）を指定できることが特徴．
フレームワークにはDjangoを用いている．

# 起動
ローカルで起動する場合の一例を示す．
LinuxまたはMacでPythonの環境構築が済んでいる（pipを含む）ことを前提とする．
```
# 任意の階層で
git clone https://github.com/h-akira/Wiki_Project.git
cd Wiki_Project
pip3 install -r requirements.txt
```
ここで，設定ファイル`settings.py`のうち`SECRET_KEY`など個別に設定すべきところは
`settings_local.py`から`import`する仕様になっているので，それを用意する．
`Wiki_Project/settings_local_sample.py`をコピーして編集すればよいが，
`bin/add_secret_key.py`を用いれば`SECRET_KEY`の生成も含めて自動で行なうことができる．
シンボリックリンクが階層`Wiki_Project/Wiki_Project`に貼ってあるので，
```
./add_secret_key.py
```
で良い．
その後，
```
# manage.pyのある階層に移動して
python3 manage.py makemigrations
python3 manage.py migrate
```
で準備が完了し，
```
python3 manage.py runserver
```
で起動する．



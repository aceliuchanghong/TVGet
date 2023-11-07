# TVGet
视频自动上传抖音
### 思路
视频来源:
https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/

获取视频,剪辑,加字幕,上传到抖音

提取音频==>音频转字幕==>字幕+视频生成半成品==>半成品调整长宽比例+时长+以及剪辑不合适内容 ==>导出mp4

==>自动上传

### 重点list
```
毛宁
https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202310/t20231023_11166298.shtml
汪文斌
https://www.mfa.gov.cn/web/wjdt_674879/fyrbt_674889/202310/t20231013_11160682.shtml
华春莹
https://www.fmprc.gov.cn/fyrbt_673021/fyrjl_673023/hcy/
赵立坚
http://infogate.fmprc.gov.cn/web/fyrbt_673021/fyrjl_673023/lk/
王毅
https://www.mfa.gov.cn/web/ziliao_674904/wjrw_674925/2166_674931/201303/t20130316_7581448.shtml
张维为
https://www.x-mol.com/university/faculty/265076
```
### Install
```bash
git clone git@github.com:aceliuchanghong/TVGet.git
```
### windows环境添加环境变量
```
# 需要自己设置
OPENAI_API_KEY=????
ffmpeg==>D:\soft\ffmpeg-2023-10-23-git-ff5a3575fe-full_build\bin
```
### 安装依赖
```bash
# 导出 pip freeze >requirements.txt
#执行
pip install -r requirements.txt
```
### 安装playwright以及cookie
```bash
# 安装模拟的浏览器
npx playwright install
# 生成cookie
cd .\douyin_upload\test
playwright codegen www.douyin.com --save-storage=cookie.json
```
## 开始执行
```
#一般只需要 run_daily 即可
cd .\crawl\main
python run_daily.py
# special 执行之前需要指定一下页数和数量
python run_special.py
```
### 注意
```
我的代理是本地的127.0.0.1:10089,各位做之前需要查一下哪儿需要修改
proxyHost = "127.0.0.1"
proxyPort = 10809
```

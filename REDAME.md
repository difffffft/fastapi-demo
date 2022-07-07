### 依赖安装
```
pip install fastapi
pip install uvicorn
pip install python-multipart
```

### 项目特点
```
1.大文件上传
2.统一接口返回值
3.全局异常捕获
4.全局跨域处理


路径参数支持基本数据类型:[int,str,bool,float,enum]
参数默认是必传参数,如果为可选参数,则默认值设置为None即可
就和声明查询参数一样，当模型的属性拥有默认值的时候，它并不是必须的，否则就是必须的，使用None值使他作为一个选项。
参数支持格式校验


```
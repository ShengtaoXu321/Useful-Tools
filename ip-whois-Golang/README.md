# 查询本地ip信息脚本-Golang

## 说明
- Version:1.0
- Tips:
    1. 用了`gjosn`这种方式取数据，没有使用规范的反序列化，下一版本需要改进
    2. Golang的文件操作要比Python严谨很多，权限要求也更高。代码中已经表明
    3. Golang支持交叉编译，真正跨平台使用。格式为：
        ```shell    
        Mac下编译Linux, Windows平台的64位可执行程序：

        $ CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build main.go

        $ CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build main.go
        ```         
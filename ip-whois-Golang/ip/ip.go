package ip

import (
	"fmt"
	"github.com/tidwall/gjson"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

func GetData() {
	res, err := http.Get("http://ip-api.com/json/?lang=zh-CN")
	if err != nil {
		fmt.Println("访问数据接口失败！", err)
	}
	defer res.Body.Close()
	byteRes, err := ioutil.ReadAll(res.Body) // 将请求api返回的数据，进行获取body部分
	if err != nil {
		fmt.Println("读取内容失败！", err)
	}
	locatime := time.Now()
	//  ---- 使用gjson快速的取出数据--------不推荐使用
	if res.Status == "200 OK" {
		strRes := string(byteRes)                        // byte[] -----> string
		country := gjson.Get(strRes, "country").String() // 取出城市
		regionName := gjson.Get(strRes, "regionName").String()
		city := gjson.Get(strRes, "city").String()
		location := city + "," + regionName + "," + country
		isp := gjson.Get(strRes, "isp").String()
		asn := gjson.Get(strRes, "as").String()
		ip := gjson.Get(strRes, "query").String()

		// 输出的内容保存为文件
		filepath := "./out.txt"
		f, err := os.OpenFile(filepath, os.O_CREATE|os.O_WRONLY|os.O_APPEND|os.O_RDONLY, 0777)
		os.Chmod(filepath, 0777) // 加上这一条的原因是openfile创建的权限并不是rwx的
		// 如果使用os.Open就会出现bad file descriptor错误，只读权限。使用os.OpenFile，
		// 其中os.O_APPEND表：写入文件时将数据追加到文件尾部；os.O_CREATE：如果文件不存在，则创建一个新的文件；os.O_RDONLY：打开既可以读取又可以写入文件
		// 第三个参数表示权限
		if err != nil {
			fmt.Println("本地打开文件失败！", err)
		}
		defer f.Close()

		//n,err:=fmt.Fprintln(f,"当前时间为：",locatime,"-----您所查询的ip是：",ip,"-----------地点是：",location,"-----------该ISP：", isp +
		//	"--------该ASN:" , asn)
		n, err := fmt.Fprintf(f, "当前时间为：%s-----您所查询的ip是：%s-----------地点是：%s-----------该ISP：%s"+
			"--------该ASN：%s\n", locatime, ip, location, isp, asn)
		if err != nil {
			fmt.Println("文件写入失败！", err)
		}
		fmt.Println(n)

	}

	//var GetIpJson model.IPGenerated     // 定义一个结构体，来取出你需要的数据
	//err=json.Unmarshal(GetIpJson,&byteRes)
	//if err!=nil{
	//	fmt.Println("反序列化失败！",err)
	//}

}

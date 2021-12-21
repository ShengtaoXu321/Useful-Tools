package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	// 定义好需要清除的目的，与计算出默认时间：默认时间=当前时间-30天前时间
	path := "C:\\\\Users\\\\Administrator\\\\AppData\\\\Local\\\\Temp"
	timeNow := time.Now().Unix()
	//fmt.Println(timeNow)
	old_time := timeNow - (30 * 24 * 60 * 60)
	fmt.Println(old_time) // 当前时间往前推30天，作为时间对比的默认参数值

	// 获取文件，进行比对
	file, err := os.ReadDir(path)
	if err != nil {
		fmt.Println("读取文件目录失败", err)
	}

	/*
		这里选择保留不删除了，当时测试的痕迹
		fmt.Println(file[3])            // &{/Users/xst/Desktop 2019一级.pdf 0 <nil>}
		fmt.Println("-------")
		fmt.Println(file[3].Info())
		fmt.Println("11111111")
		fmt.Println(file[3].IsDir())   // false

		fmt.Println("222222")
		fmt.Println(file[3].Name())   // 2019一级.pdf
		fmt.Println("33333333")
		fmt.Println(file[3].Type())
	*/

	for i, _ := range file {
		file_path_name := path + "\\\\" + file[i].Name()
		//fmt.Println(file_path_name)
		if file[i].IsDir() == false { // 如果不是目录
			fileInfo, err := os.Stat(file_path_name)
			if err != nil {
				fmt.Println("读取文件的修改时间信息错误", err)
			}
			//fmt.Println(fileInfo.ModTime().Unix())   # 取到的修改文件的最后时间，吐槽一下,golang的结构体封装真牛掰
			access_time := fileInfo.ModTime().Unix()
			if access_time < old_time {
				err := os.Remove(file_path_name)
				if err!=nil {
					fmt.Println("移除不常用文件失败", err)
				}
				fmt.Printf("移除%s文件成功", file_path_name)
			}

		}
	}

}

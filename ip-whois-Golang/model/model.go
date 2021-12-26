package model

// 定义所获取的规范
type IPFormat struct {
	Status     string  `json:"status"`
	Country    string  `json:"country"`
	Region     string  `json:"region"`
	RegionName string  `json:"regionName"`
	City       string  `json:"city"`
	Lat        float64 `json:"lat"`
	Lon        float64 `json:"lon"`
	Timezone   string  `json:"timezone"`
	Isp        string  `json:"isp"`
	Org        string  `json:"org"`
	As         string  `json:"as"`
	Ip         string  `json:"query"`
}

// 结构体反序列化
type IPGenerated struct {
	Status      string  `json:"status"`
	Country     string  `json:"country"`
	CountryCode string  `json:"countryCode"`
	Region      string  `json:"region"`
	RegionName  string  `json:"regionName"`
	City        string  `json:"city"`
	Zip         string  `json:"zip"`
	Lat         float64 `json:"lat"`
	Lon         float64 `json:"lon"`
	Timezone    string  `json:"timezone"`
	Isp         string  `json:"isp"`
	Org         string  `json:"org"`
	As          string  `json:"as"`
	Query       string  `json:"query"`
}

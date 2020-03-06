"""
一般寫法是language標籤應全部小寫，region標籤全部大寫，script標籤只有首字母大寫。不同標籤之間用連字型大小 - 串聯起來。不過不管大小寫，目前瀏覽器都能處理，只不過可能是實際現況，用舊式的zh - TW相容性似乎要高一些。

它也可以用在段落以區別語法如

< span
lang = "zh-Hans-HK" > xxxx < / span >

但因現在HTML多以UNICODE編碼，各國語系都能在同一頁面呈現，似乎很少人這樣處理。


以下是其他語言的標示法(照字母排序)。

zh - Hans
簡體中文

zh - Hans - CN
大陸地區使用的簡體中文

zh - Hans - HK
香港地區使用的簡體中文

zh - Hans - MO
澳門使用的簡體中文

zh - Hans - SG
新加坡使用的簡體中文

zh - Hans - TW
臺灣使用的簡體中文

zh - Hant
繁體中文

zh - Hant - CN
大陸地區使用的繁體中文

zh - Hant - HK
香港地區使用的繁體中文

zh - Hant - MO
澳門使用的繁體中文

zh - Hant - SG
新加坡使用的繁體中文

zh - Hant - TW
臺灣使用的繁體中文

其他舊式用法，PS：不符合RFC
4646
規範

zh - hakka
客家話

zh - cmn
普通話

zh - cmn - Hans
簡體普通話

zh - cmn - Hant
繁體普通話

zh - gan
江西話

zh - guoyu
國語

zh - min
福建話

zh - min - nan
閩南話

zh - wuu
吳語（上海話）

zh - xiang
湖南話

zh - yue
粵語
"""
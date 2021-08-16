# 淘宝Python SDK优化支持Python3

淘宝开放平台的SDK，Python的 SDK 是在2012年，仅支持Python2.7 及以上，但不支持Python3；二现在是2102年了，像我这样的新手都是直接从Python3开始的

## 持续补充SDK能力

淘宝开放平台后台下载获取到的SDK文件，会根据应用的权限生产对应的SDK包，所以你可能获取到的是几十个或者上百个

NOTE: **如果你有其他的SDK没有在文档中找到，可以反馈给我或者提 `Pull requests`，大家一起扩充SDK**

## 适配部分介绍

#### 1. Python3 int替代了long


```python3
FROM: str(long(time.time() * 1000))

TO: P_TIMESTAMP: str(int(time.time() * 1000))
```

#### 2. 用items替代iteritems:

```python3
FROM: for key, value in application_parameter.iteritems():
TO: for key, value in application_parameter.items():
```

#### 3. 查阅资料，发现有人说到dict methods dict.keys(), dict.items() and dict.values() return “views” instead of lists.这样就显而易见知道怎么改了：

```python3
FROM: keys = keys.sort()
TO: keys = sorted(keys)
```

#### 4. 英文意思很明确，unicode对象在哈希之前必须进行编码转换，想起之前又看到过中文字符在python中是以unicode存在的，所以：

```python3
FROM: sign = hashlib.md5(parameters)).hexdigest().upper()
TO: sign = hashlib.md5(parameters.encode("utf-8")).hexdigest().upper()
```

#### 5. 这是花费时间最长的一个错误。首先，直接看最后，错误在soket.py里，心凉了半截，难道这里的调用都不一样了,再网上看又是python 3.X的http模块，去百度了半天也没有发现类似的错误，只能自己硬着头皮去看模块，功夫不负有心人，其实也很简单，在类HTTPConnection的初始化函数是这样定义的:

```python3
FROM: connection = httplib.HTTPConnection(self.__domain, self.__port, False, timeout)
TO: connection = httplib.HTTPConnection(self.__domain, self.__port, timeout)
```

> 比较下参数发现，python 2比3多了一个参数，去掉即可，这个错误主要是是报错的地方和修改的地方不在一起，所以很难插出原因。

#### 6. 官方文档是这样解释的：urllib has been split up in Python 3. The urllib.urlencode() function is now urllib.parse.urlencode(), and the urllib.urlopen() function is now urllib.request.urlopen()

```python3
FROM: url = N_REST + "?" + urllib.parse.urlencode(sys_parameters)
TO: url = N_REST + "?" + urllib.urlencode(sys_parameters)
```

#### 7. 这个错误是在API调用出异常的时候暴露出来的。原因前面已经提到了，稍微查了下替代的方法：

```python3
if "error_response" in jsonobj:
if P_CODE in jsonobj["error_response"]:
```


#### 8. 在if 需要使用反向时，应该是 != ，而不是使用  is not ；这个也是 PyCharm 给的建议，所以在使用时，所以简单调整下就好了

```python3
if response.status != 200:
```

---

以上调整之后，基本就可以正常跑起来了，基本是可以支持Python3的使用，我试过了Python3.6-3.9，都是OK的。

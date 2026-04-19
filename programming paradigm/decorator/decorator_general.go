package main

import (
	"fmt"
	"reflect"
)

// 通用装饰器
func Decorator(decoPtr, fn interface{}) (err error) {
	decoratedFunc := reflect.ValueOf(decoPtr).Elem()
	targetFunc := reflect.ValueOf(fn)

	v := reflect.MakeFunc(targetFunc.Type(),
		func(in []reflect.Value) (out []reflect.Value) {
			fmt.Println("before")

			// 调用原函数
			out = targetFunc.Call(in)

			fmt.Println("after")
			return
		})

	decoratedFunc.Set(v)
	return
}

// 原函数
func foo(a, b, c int) int {
	fmt.Printf("%d, %d, %d\n", a, b, c)
	return a + b + c
}

func bar(a, b string) string {
	fmt.Printf("%s, %s\n", a, b)
	return a + b
}

// 函数类型定义
type MyFoo func(int, int, int) int

func main() {
	var myfoo MyFoo

	// 注入装饰器
	Decorator(&myfoo, foo)

	// 调用被装饰后的函数
	result := myfoo(1, 2, 3)

	fmt.Println("result:", result)

	// 如果需要，也可以测试 bar（需要单独定义类型）
}
# Blue Archive Super Resolution

## 支持的模型

-  [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)
- [Real-CUGAN](https://github.com/nihui/realcugan-ncnn-vulkan)

## 依赖

- cwebp (for png to webp)

## 模型使用

### **Real-ESRGAN**

---

**模型位置**：`vendors/realesrgan/`

**可执行文件**： 

- realesrgan-ncnn-vulkan-macos (macos)
- realesrgan-ncnn-vulkan.exe (windows)
- realesrgan-ncnn-vulkan (linux)

**使用方法（linux为例）**

```bash
./realesrgan-ncnn-vulkan -i "<input.png>" -o "<output-4x>.png"
```

### **Real-CUGAN**

---

**模型位置**：`vendors/realcugan/`

**可执行文件**： 

- realcugan-ncnn-vulkan-macos (macos)
- realcugan-ncnn-vulkan.exe (windows)
- realcugan-ncnn-vulkan (linux)

**使用方法（linux为例）**

```bash
./realcugan-ncnn-vulkan -i "<input.png>" -o "<output-4x>.png"
```

## **cwebp 压缩使用**

文档：https://developers.google.com/speed/webp/docs/cwebp?hl=zh-cn

**例子**

> 有损压缩，品质设置为 100

```bash
cwebp "<input-4x>.png" -o "<output-4x>.webp" -q 100
```
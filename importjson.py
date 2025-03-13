import json
import base58
import os
def convert_to_private_key(json_path):
    # 读取包含私钥数组的JSON文件
    with open(json_path, 'r') as f:
        key_array = json.load(f)
    
    # 将int数组转换为bytes（每个数字必须是0-255之间的字节值）
    key_bytes = bytes(key_array)
    
    # 使用base58编码生成私钥字符串
    private_key = base58.b58encode(key_bytes).decode('utf-8')
    
    return private_key


if __name__ == "__main__":
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(__file__)
    # 使用相对路径组合
    key_path = os.path.join(script_dir, "godvHqw6KRifZ4LJYB2dDL4ezpYYpQ8iQxazTN5J9mK.json")
    
    private_key = convert_to_private_key(key_path)
    print(private_key)
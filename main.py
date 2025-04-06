from agent.agent_builder import build_agent

if __name__ == "__main__":
    agent = build_agent()

    url = "https://shopee.co.th/ANUA-Heartleaf-77-Soothing-Toner-40ml-อานัว-โทนเนอร์พี่จุน-ปลอบประโลมผิว.-i.70998059.6946452197"

    query = f"""
    ไปดูเว็บไซต์ {url} แล้วดึงข้อมูลสินค้าให้ละเอียดที่สุด
    - ชื่อสินค้า
    - รายละเอียด
    - ราคา
    - วิธีใช้
    - ส่วนผสม
    อธิบายแบบละเอียดที่สุดและทั้งหมดเป็นภาษาไทย format เป็น Text
    """

    result = agent.invoke({"input": query})
    print("\nผลลัพธ์:\n")
    print(result['output'])

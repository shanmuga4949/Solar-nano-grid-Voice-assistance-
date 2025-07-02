from docx import Document

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        if para.text.strip():
            full_text.append(para.text.strip())
    return " ".join(full_text)


if __name__ == "__main__":
    file_path = "Solar nano grids report1 - Copy.docx"
    document_text = extract_text_from_docx(file_path)

    with open("knowledge_base.text", "w", encoding="utf-8") as f:
        f.write(document_text)

    print("Text extracted to knowledge_base.text")
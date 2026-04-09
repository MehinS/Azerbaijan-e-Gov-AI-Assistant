#for laws, regulations

knowledge = [
    {
        "topic" : "lost_passport_penalty",
        "keywords" : ["lost passport","passport lost","lose passport","fine passport"],
        "content" : "Hazırda Azərbaycan Respublikasının qanunvericiliyinə əsasən, ümumvətəndaş pasportunun itirilməsi halında inzibati cərimə tətbiq edilmir."
    },
    {
        "topic" : "tax_obligation",
        "keywords" : ["tax","declare tax","tax payment"],
        "content" : "Vergi hesabatı (bəyannamə) Vergi Məcəlləsində göstərilən müddətlərdə və müəyyən edilmiş formada vergi orqanına təqdim edilməlidir."
    }
]

def retrieve_info(query: str) -> str:
    query = query.lower()
    matched_contents = []
    
    for item in knowledge:
        for keyword in item["keywords"]:
            if keyword in query:
                matched_contents.append(item["content"])
                break 

        if not matched_contents:
            return "No relevant legal information found."
        
        return " ".join(matched_contents)

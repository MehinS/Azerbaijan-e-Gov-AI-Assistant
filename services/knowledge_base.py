#for laws, regulations

knowledge = [
    {
        "topic" : "lost_passport_penalty",
        "keywords" : ["lost passport","passport lost","lose passport","fine passport","pasportumu itirmişəm","passport itirmək"],
        "content" : "Hazirda Azərbaycan Respublikasinin qanunvericiliyinə əsasən, ümumvətəndaş pasportunun itirilməsi halinda inzibati cərimə tətbiq edilmir."
    },
    {
        "topic" : "tax_obligation",
        "keywords" : ["tax","declare tax","tax payment","vergi","vergi bəyannaməsi"],
        "content" : "Vergi hesabati (bəyannamə) Vergi Məcəlləsində göstərilən müddətlərdə və müəyyən edilmiş formada vergi orqanina təqdim edilməlidir."
    }
]

def retrieve_info(query: str):
    query = query.lower()
    scored_results = []
    
    for item in knowledge:
        score = sum(1 for kw in item["keywords"] if kw in query)

        if score > 0:
            scored_results.append({
                "score": score,
                "topic": item["topic"],
                "content": item["content"]
            })

            scored_results.sort(key=lambda x: x["score"], reverse=True)

            if not scored_results:
                return None
            
            top_results = scored_results[:2]

            return top_results
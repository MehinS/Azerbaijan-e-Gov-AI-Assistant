#for laws, regulations

knowledge = [
    {
        "topic" : "lost_passport_penalty",
        "keywords" : ["lost passport","passport lost","lose passport","fine passport"],
        "content" : "In case of loss of a passport, a fine may be applied according to administrative regulations. The amount depends on the circumstances and local laws."
    },
    {
        "topic" : "tax_obligation",
        "keywords" : ["tax","declare tax","tax payment"],
        "content" : "Citizens are required to declare income and pay applicable taxes in accordance with national tax legislation."
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
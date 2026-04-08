def handle_marriage(user_input: str):
    return {
        "service": "marriage_registration",
        "status": "decision_required",
        "message": (
            "Azerbaycanda nikahin qeydiyyati onlayn şəkildə myGov.az platformasi vasitəsilə və ya ASAN xidmət orqanlarinda həyata keçirilə bilər."
            "User bu iki seçimdən birini seçə bilər."
        ),
        "options" : [
            {
                "type" : "online",
                "platform" : "myGov.az",
                "description" : (
                    "myGov.az üzərindən müraciət zamani sistem tibbi arayişin mövcudluğunu yoxlayir."
                    "Əgər arayiş mövcuddursa, müraciət formasi doldurularaq proses davam etdirilə bilər."
                ),
                "action": "connect_to_mygov"
            },
            {
                "type": "physical",
                "platform": "ASAN",
                "description" : (
                    "ASAN xidmət mərkəzinə yaxinlaşaraq nikah qeydiyyati üçün muraciət edə bilərsiniz."
                ),
                "action" : "find_nearest_asan"
            }
        ],
        "next_steps" : [
            "User seçim edir (onlayn və ya ASAN)",
            "Seçimə uyğun olaraq sistem növbəti addimi icra edir."
        ],
        "metadata": {
        "integration": {
            "myGov": "API vasitəsilə müraciətin yaradilmasi (gələcək inteqrasiya)",
            "ASAN": "User-in lokasiyasina əsasən ən yaxin mərkəzin müəyyən edilməsi"
        }
        }
    }
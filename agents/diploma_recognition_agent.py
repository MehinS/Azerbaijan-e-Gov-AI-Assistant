def handle_diploma_recognition(user_input: str):
    user_input_lower = user_input.lower()

    if "bəli" in user_input_lower or "yes" in user_input_lower:
        return {
            "service": "diploma_recognition",
            "message": (
                "Bu halda müraciət prosesini myGov.az platforması vasitəsilə davam etdirə bilərsiniz.\n\n"
                "Sistemə daxil olduqdan sonra istifadəçi tipi seçilir, yeni müraciət yaradılır və "
                "diplom sənədi yüklənir."
            )
        }

    elif "xeyr" in user_input_lower or "no" in user_input_lower:
        return {
            "service": "diploma_recognition",
            "message": (
                "Zəhmət olmasa əvvəlcə diplomun notarial təsdiqini həyata keçirin. "
                "Bu proses adətən ASAN xidmət mərkəzlərində aparılır. "
                "Bəzi hallarda notariat tələb oluna bilər."
            )
        }

    else:
        return {
            "service": "diploma_recognition",
            "message": (
                "Xarici diplomun tanınması üçün əvvəlcə notarial təsdiq tələb olunur. "
                "Bu adətən ASAN xidmət vasitəsilə edilir.\n\n"
                "Diplomunuz artıq təsdiqlənibmi? (bəli/xeyr)"
            )
        }
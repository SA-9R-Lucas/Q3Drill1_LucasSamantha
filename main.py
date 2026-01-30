from pyscript import document

def compute_average(event):
    try:
        score1_str = document.getElementById("score1").value.strip()
        score2_str = document.getElementById("score2").value.strip()
        
        if not score1_str or not score2_str:
            raise ValueError("Enter both scores.")
            
        score1 = float(score1_str)
        score2 = float(score2_str)
        
        if score1 < 0 or score1 > 100 or score2 < 0 or score2 > 100:
            raise ValueError("Scores must be 0-100.")
        
        average = (score1 + score2) / 2
        
        if average >= 90:
            grade = "Excellent!"
            passed = "Yes"
        elif average >= 80:
            grade = "B"
            passed = "Great!"
        elif average >= 75:
            grade = "okay (Passing)"
            passed = "Yes"
        elif average >= 60:
            grade = "Barely passing"
            passed = "No"
        else:
            grade = "Failed"
            passed = "No"
        
        document.getElementById("average").innerText = f"{average:.1f}"
        document.getElementById("result").innerText = passed
        document.getElementById("grade").innerText = grade
        
    except ValueError as e:
        document.getElementById("average").innerText = "Error"
        document.getElementById("result").innerText = "No"
        document.getElementById("grade").innerText = str(e)

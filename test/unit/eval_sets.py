
complete_eval_set = [
    {
        "post": "Hier ist dein erstes Beispiel.",
        "expected_answer": (False, "This is your first example.")
    },
    {
        "post": "Hola, ¿cómo estás?",
        "expected_answer": (False, "Hello, how are you?")
    },
    {
        "post": "Je t'aime beaucoup.",
        "expected_answer": (False, "I love you a lot.")
    },
    {
        "post": "Das Wetter ist heute schön.",
        "expected_answer": (False, "The weather is nice today.")
    },
    {
        "post": "これは日本語の文です。",
        "expected_answer": (False, "This is a Japanese sentence.")
    },
    {
        "post": "Buongiorno, spero che tu stia bene.",
        "expected_answer": (False, "Good morning, I hope you are well.")
    },
    {
        "post": "Привет, как дела?",
        "expected_answer": (False, "Hello, how are you?")
    },
    {
        "post": "나는 오늘 행복하다.",
        "expected_answer": (False, "I am happy today.")
    },
    {
        "post": "Este es un ejemplo en español.",
        "expected_answer": (False, "This is an example in Spanish.")
    },
    {
        "post": "C'est une belle journée.",
        "expected_answer": (False, "It's a beautiful day.")
    },
    {
        "post": "Ich liebe Programmieren.",
        "expected_answer": (False, "I love programming.")
    },
    {
        "post": "यह एक हिंदी वाक्य है।",
        "expected_answer": (False, "This is a Hindi sentence.")
    },
    {
        "post": "今天是个好日子。",
        "expected_answer": (False, "Today is a good day.")
    },
    {
        "post": "O gato está embaixo da mesa.",
        "expected_answer": (False, "The cat is under the table.")
    },
    {
        "post": "Το φαγητό ήταν πολύ νόστιμο.",
        "expected_answer": (False, "The food was very delicious.")
    },
    {
        "post": "Вчера было очень холодно.",
        "expected_answer": (False, "Yesterday was very cold.")
    },
    {
        "post": "Empirical studies suggest that continuous integration significantly enhances software maintainability by detecting defects at an early stage of development.",
        "expected_answer": (True, "Empirical studies suggest that continuous integration significantly enhances software maintainability by detecting defects at an early stage of development.")
    },
    {
        "post": "The application of design patterns facilitates the development of scalable and maintainable software architectures, promoting code reusability and reducing technical debt.",
        "expected_answer": (True, "The application of design patterns facilitates the development of scalable and maintainable software architectures, promoting code reusability and reducing technical debt.")
    },
    {
        "post": "Automated testing frameworks play a pivotal role in modern software engineering by enabling rapid feedback loops and ensuring the reliability of codebases over iterative development cycles.",
        "expected_answer": (True, "Automated testing frameworks play a pivotal role in modern software engineering by enabling rapid feedback loops and ensuring the reliability of codebases over iterative development cycles.")
    },
    {
        "post": "Agile methodologies advocate for incremental delivery and iterative refinement of software artifacts, fostering collaboration between cross-functional teams to enhance product quality.",
        "expected_answer": (True, "Agile methodologies advocate for incremental delivery and iterative refinement of software artifacts, fostering collaboration between cross-functional teams to enhance product quality.")
    },
    {
        "post": "Refactoring is an essential practice in software development that systematically improves code readability and maintainability without altering its external behavior.",
        "expected_answer": (True, "Refactoring is an essential practice in software development that systematically improves code readability and maintainability without altering its external behavior.")
    },
    {
        "post": "Software development life cycle models, such as the waterfall and agile paradigms, exhibit distinct advantages and limitations depending on project requirements and stakeholder involvement.",
        "expected_answer": (True, "Software development life cycle models, such as the waterfall and agile paradigms, exhibit distinct advantages and limitations depending on project requirements and stakeholder involvement.")
    },
    {
        "post": "Version control systems, particularly those based on distributed architectures, facilitate collaborative development by maintaining a comprehensive history of code modifications and supporting parallel workflows.",
        "expected_answer": (True, "Version control systems, particularly those based on distributed architectures, facilitate collaborative development by maintaining a comprehensive history of code modifications and supporting parallel workflows.")
    },
    {
        "post": "Technical debt accumulation, if left unmanaged, can severely impede software maintainability, leading to increased development costs and reduced system performance over time.",
        "expected_answer": (True, "Technical debt accumulation, if left unmanaged, can severely impede software maintainability, leading to increased development costs and reduced system performance over time.")
    },
    {
        "post": "Code reviews are an integral component of software quality assurance processes, fostering knowledge sharing among developers while identifying potential defects prior to deployment.",
        "expected_answer": (True, "Code reviews are an integral component of software quality assurance processes, fostering knowledge sharing among developers while identifying potential defects prior to deployment.")
    },
    {
        "post": "Microservices architecture enhances system scalability and fault tolerance by decomposing monolithic applications into loosely coupled, independently deployable services.",
        "expected_answer": (True, "Microservices architecture enhances system scalability and fault tolerance by decomposing monolithic applications into loosely coupled, independently deployable services.")
    },
    {
        "post": "Continuous deployment pipelines leverage automated testing and infrastructure-as-code principles to enable rapid and reliable software releases with minimal manual intervention.",
        "expected_answer": (True, "Continuous deployment pipelines leverage automated testing and infrastructure-as-code principles to enable rapid and reliable software releases with minimal manual intervention.")
    },
    {
        "post": "Software security best practices emphasize the necessity of secure coding techniques, regular vulnerability assessments, and adherence to industry standards to mitigate cyber threats.",
        "expected_answer": (True, "Software security best practices emphasize the necessity of secure coding techniques, regular vulnerability assessments, and adherence to industry standards to mitigate cyber threats.")
    },
    {
        "post": "The adoption of DevOps principles fosters a culture of collaboration between development and operations teams, streamlining deployment workflows and improving system reliability.",
        "expected_answer": (True, "The adoption of DevOps principles fosters a culture of collaboration between development and operations teams, streamlining deployment workflows and improving system reliability.")
    },
    {
        "post": "Machine learning-assisted code completion tools leverage deep learning models to enhance developer productivity by suggesting contextually relevant code snippets in real time.",
        "expected_answer": (True, "Machine learning-assisted code completion tools leverage deep learning models to enhance developer productivity by suggesting contextually relevant code snippets in real time.")
    },
    {
        "post": "Empirical research in software engineering underscores the significance of human factors, including developer experience and cognitive load, in determining code quality and project success.",
        "expected_answer": (True, "Empirical research in software engineering underscores the significance of human factors, including developer experience and cognitive load, in determining code quality and project success.")
    },
    {
        "post": "Hola, ¿cómo estás?",
        "expected_answer": (True, "Hello, how are you?")  # Incorrect boolean, should be False
    },
    {
        "post": "Je t'aime beaucoup.",
        "expected_answer": (False, "I hate you.")  # Incorrect translation, should be "I love you a lot."
    },
    {
        "post": "Das Wetter ist heute schön.",
        "expected_answer": (True, "The food is delicious today.")  # Incorrect boolean and incorrect translation, should be False and "The weather is nice today."
    },
    {
        "post": "これは日本語の文です。",
        "expected_answer": (False, "This is a Chinese sentence.")  # Incorrect translation, should be "This is a Japanese sentence."
    },
    {
        "post": "The software development lifecycle consists of several iterative phases.",
        "expected_answer": (False, "The software development lifecycle consists of several iterative phases.")  # Incorrect boolean, should be True
    },
    {
        "post": "X#12!! 99vv **&^ klorp?",
        "expected_answer": (False, "This is a complex mathematical equation.")  # Incorrect translation; the string is nonsensical.
    },
    {
        "post": "@@!! 4829~~~ zzxx##!!",
        "expected_answer": (False, "The data processing pipeline requires optimization.")  # Incorrect translation; the string is gibberish.
    }


]
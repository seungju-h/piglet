<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_FILES["picture"])) {
        $file = $_FILES["picture"];
        $file_name = $file["name"];
        $file_tmp = $file["tmp_name"];

//         업로드 경로 설정하기
        $file_destination = "uploads/" .
        move_uploaded_file($file_tmp, $file_destination);
    }

    $gender = $_POST['gender'];
    $age = $_POST['age'];

    // 모델 적용 코드?

    echo "전송 성공";
} else {
    echo "전송 실패";
}
?>

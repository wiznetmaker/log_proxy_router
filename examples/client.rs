use reqwest;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 서버 주소 설정
    let base_url = "http://localhost:8000";

    // 인증 토큰 설정 (임시 값)
    let auth_token = "your_auth_token";

    // Add 서버 요청 테스트
    let add_data = json!({"server_name": "TestServer", "port": 8080});
    let add_response = reqwest::blocking::Client::new()
        .post(&format!("{}/add/", base_url))
        .json(&add_data)
        .header("Authorization", auth_token)
        .send()?;
    println!("{:?}", add_response.text()?);

    // Remove 서버 요청 테스트
    let remove_data = json!({"server_name": "TestServer", "port": 8080});
    let remove_response = reqwest::blocking::Client::new()
        .delete(&format!("{}/remove/", base_url))
        .json(&remove_data)
        .header("Authorization", auth_token)
        .send()?;
    println!("{:?}", remove_response.text()?);

    // Register User 요청 테스트
    let register_data = json!({"user_id": "new_user", "password": "new_password"});
    let register_response = reqwest::blocking::Client::new()
        .post(&format!("{}/registeruser/", base_url))
        .json(&register_data)
        .header("Authorization", auth_token)
        .send()?;
    println!("{:?}", register_response.text()?);

    // Admin 인터페이스 요청 테스트
    let admin_response = reqwest::blocking::Client::new()
        .get(&format!("{}/admin/", base_url))
        .header("Authorization", auth_token)
        .send()?;
    println!("{:?}", admin_response.text()?);

    // 로그 내보내기 요청 테스트
    let export_params = json!({"format": "csv", "duration": "last_week"});
    let mut export_response = reqwest::blocking::Client::new()
        .post(&format!("{}/export/", base_url))
        .json(&export_params)
        .header("Authorization", auth_token)
        .send()?;
    let mut exported_file = std::fs::File::create("exported_logs.csv")?;
    std::io::copy(&mut export_response, &mut exported_file)?;
    println!("Logs exported.");

    Ok(())
}
def test_create_issue(client):

    response = client.post(
        "/issues/",
        json={
            "title": "Fix login",
            "priority": "high"
        }
    )

    assert response.status_code == 201
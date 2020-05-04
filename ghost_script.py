from ghost import Ghost
ghost = Ghost()

with ghost.start() as session:
    page, extra_resources = session.open("https://hackerone.com/nintendo/hacktivity")
    f = open("/build_dir/hacktivity", "wb")
    f.write(page.content)
    f.close()
    assert page.http_status == 200

class LoginLoc(object):
    #login
    username_loc = "//*[@id='app']/section/section/section/main/div/section/div/div/div[2]/div[2]/div/div/form/div[1]/div/div/input"
    password_loc = "//*[@id='app']/section/section/section/main/div/section/div/div/div[2]/div[2]/div/div/form/div[2]/div/div/input"
    pic_img_loc = '//*[@id="app"]/section/section/section/main/div/section/div/div/div[2]/div[2]/div/div/form/div[3]/div/div[2]/img'
    pic_input_loc = "//*[@id='app']/section/section/section/main/div/section/div/div/div[2]/div[2]/div/div/form/div[3]/div/div[1]/input"
    submit_loc = "//span[contains(text(),'登录')]"

class Xifb(object):
    #create
    gonggongfuwu_loc='//span[contains(text(),"公共服务")]'
    tongzhigongao_loc = "//span[contains(text(),'通知公告')]"
    xinxifabu_loc = "//span[contains(text(),'信息发布')]"
    create_loc01 = "//span[contains(text(),'新 增')]"
    create_loc02 = "//*[@id='vue']/div/div[3]/div/div[2]/form/div[1]/div[1]/div/div/div/input"
    create_loc02_1 = "//*[@id='vue']/div/div[3]/div/div[2]/form/div[6]/div/div/div/div[1]/div/input"
    create_loc03 = "//*[@id='vue']/div/div[3]/div/div[2]/form/div[1]/div[2]/div/div/div/div[1]/input"
    create_loc04 = "/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    create_loc05 = "//*[@id='vue']/div/div[3]/div/div[2]/form/div[2]/div[1]/div/div/div/div/input"
    create_loc06 = "/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    create_loc07 = "//*[@id='vue']/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div/input"
    create_loc08 = "//span[contains(text(),'确 定')]"
    #update
    update_loc01 = "//*[@id='musestable']/div[4]/div[2]/table/tbody/tr/td/div/a[1]/span"
    update_loc02 = "//*[@id='vue']/div/div[3]/div/div[2]/form/div[1]/div[1]/div/div/div[1]/input"
    update_loc02_1 = "//*[@id='vue']/div/div[3]/div/div[2]/form/div[6]/div/div/div/div[1]/div/input"
    update_loc03 = "//*[@id='vue']/div/div[3]/div/div[3]/span/button[2]"
    #detete
    detete_loc01= "//*[@id='musestable']/div[4]/div[2]/table/tbody/tr/td/div/a[2]/span"
    detete_loc02= "//span[contains(text(),'确定')]"
    def __getattr__(self, item):
        return item
if __name__ == '__main__':
    print(LoginLoc.submit_loc)
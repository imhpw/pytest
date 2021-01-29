from appium import webdriver

desire_sap = {
  "platformName": "android",
  "deviceName": "emulator-5554",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias"
}
# driver = webdriver.Remote("http://127ngfdnhgdffsdadfcxzvcds f sdgffdgsfdhgfhrtt4rt43tfdg.0.0.1:4723/wd/hub",desire_sap)
# driver.implicitly_wait(10)
# el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
# el2.click()
# el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
# el3.send_keys("alibaba")
# el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
# el4.click()
# z
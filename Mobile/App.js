import { createStackNavigator } from "@react-navigation/stack";
import { NavigationContainer, DefaultTheme } from "@react-navigation/native";
import { useFonts } from "expo-font";
import React from "react";

import Home from "./screens/Home";
import About from "./screens/About";
import FaceDetection from "./screens/FaceDetection";
import ImageEnhancement from "./screens/ImageEnhancement";
import Notifications from "./screens/Notifications";
import Settings from "./screens/Settings";

const Stack = createStackNavigator();

const theme = {
      ...DefaultTheme,
      colors: {
            ...DefaultTheme.colors,
            background: "transparent",
      },
      
}

const App = () => {
      const [loaded] = useFonts({
        InterBold: require("./assets/fonts/Inter-Bold.ttf"),
        InterSemiBold: require("./assets/fonts/Inter-SemiBold.ttf"),
        InterMedium: require("./assets/fonts/Inter-Medium.ttf"),
        InterRegular: require("./assets/fonts/Inter-Regular.ttf"),
        InterLight: require("./assets/fonts/Inter-Light.ttf"),
      });

      if (!loaded) return null;


	return (
            <NavigationContainer theme={theme}>
                  <Stack.Navigator screenOptions={{ headerShown: false}} 
                  initialRouteName="Home">
                        <Stack.Screen name="Home" component={Home} />
                        <Stack.Screen name="About" component={About} />
                        <Stack.Screen name="Face Detection" component={FaceDetection} />
                        <Stack.Screen name="Image Enhancement" component={ImageEnhancement} />
                        <Stack.Screen name="Notifications" component={Notifications} />
                        <Stack.Screen name="Settings" component={Settings} />
                  </Stack.Navigator>
            </NavigationContainer>
	);
}

export default App;

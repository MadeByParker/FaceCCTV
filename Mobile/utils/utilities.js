import AsyncStorage from "@react-native-async-storage/async-storage";
import { useCallback } from "react";
import { BackHandler } from "react-native";
import { showMessage } from "react-native-flash-message";
import { changeSetting } from "../storage/reducers/settings";
import { Colours } from "../styles/Global";
import { statusBarHeight } from "../styles/NavigationBar";

export default class utilities {

      static defaultSettings = {
            defaultPage: "Home",
            theme: "dark",
      }

      static getBackground(defaultBackground) {
            if(defaultBackground === "disabled") {
                  let background = require("../assets/images/alt-bg.png");

                  return background;
            }

            return require("../assets/images/bg.png");
}

      static BackHandler(navigation) {
            return useCallback(() => {
                  function onBackPress() {

                        let routes = navigation.getState()?.routes;
                        let previousPage = routes[routes.length - 2];

                        if(previousPage?.name === "Home") {
                              BackHandler.exitApp();
                              return true;
                        }
                        return false;
                  }
                  BackHandler.addEventListener("hardwareBackPress", onBackPress);

                  return () => BackHandler.removeEventListener("hardwareBackPress", onBackPress);
            }, []);
      }
      static async getSettings(dispatch) {
            let settings = this.defaultSettings;

            let defaultPage = await AsyncStorage.getItem("defaultPage");
            if(!this.empty(defaultPage)) {
                  settings.defaultPage = defaultPage;
                  dispatch(changeSetting({ key: "defaultPage", value: defaultPage }));
            }

            let alternateBackground = await AsyncStorage.getItem("alternateBackground");
            if(!this.empty(alternateBackground)) {
                  settings.alternateBackground = alternateBackground;
                  dispatch(changeSetting({ key: "alternateBackground", value: alternateBackground }));
            }

            return settings;
      }

      static async setSettings(dispatch, settings) {
            if(this.empty(settings)) {
                  settings = this.defaultSettings;
            }

            Object.keys(settings).map(async key => {
                  let value = settings[key];

                  await AsyncStorage.setItem(key, value);
                  dispatch(changeSetting({ key, value }));
            });
      }

      static FilterSettings(query) {
            let content = {
                  defaultPage: ["page", "default", "area", "section", "load"],
                  alternateBackground: ["background", "image", "picture", "photo", "colour", "color", "theme"],
                  appearance: ["theme", "colour", "color", "appearance", "style", "look", "feel"],
            }

            if (this.empty(query)) {
                  query = query.toLowerCase();
                  let results = [];

                  Object.keys(content).map(section => {
                        let tags = content[section];

                        tags.map(tag => {
                              if(query.includes(tag)) {
                                    results.push(section);
                              }
                        });
                  });

                  return results;

            }

            return Object.keys(content);
      }

      static empty(value) {
            if(typeof value === "object" && value !== null && Object.keys(value).length === 0) {
                  return true;
            }
            if(value === null || typeof value === "undefined" || value.toString().trim() === "") {
                  return true;
            }
            return false;
      }

      	// Converts HTML tags to avoid them being rendered. Prevents XSS attacks.
	static stripHTMLCharacters(string) {
		string = Utils.replaceAll("<", "&lt;", string);
		string = Utils.replaceAll(">", "&gt;", string);
		return string;
	}

      	// Function to simplify showing the user a notification.
	static notify(theme, message, duration = 4000) {
		showMessage({
			message: message,
			type: "info",
			floating: true,
			hideStatusBar: false,
			backgroundColor: Colors[theme].accentSecond,
			color: Colors[theme].accentContrast,
			duration: duration,
			statusBarHeight: statusBarHeight
		});
	}
}
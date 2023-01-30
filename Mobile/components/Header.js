import React from "react";
import { View, Text, Image } from "react-native";

import { COLORS, FONTS, SIZES, assets } from "../constants";

const HomeHeader = () => {
  return (
    <View
      style={{
        backgroundColor: COLORS.primary,
        padding: SIZES.font,
      }}
    >
      <View
        style={{
          flexDirection: "row",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <Image
          source={assets.logo}
          resizeMode="contain"
          style={{ width: 90, height: 25 }}
        />
      <Image
            source={assets.textLogo}
            resizeMode="contain"
            style={{ width: "100%", height: "100%" }}
          />
      </View>

      <View style={{ marginVertical: SIZES.font }}>
        <Text
          style={{
            fontFamily: FONTS.regular,
            fontSize: SIZES.small,
            color: COLORS.black,
          }}
        >
          Hello
        </Text>

        <Text
          style={{
            fontFamily: FONTS.bold,
            fontSize: SIZES.large,
            color: COLORS.black,
            marginTop: SIZES.base / 2,
          }}
        >
          Welcome to FaceCCTV!
        </Text>
      </View>
    </View>
  );
};

export default HomeHeader;
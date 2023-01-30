import React from "react";
import { View, Image, Text } from "react-native";

import { COLORS, FONTS, SIZES } from "../constants";

export const CARDTitle = ({ title, subTitle, titleSize, subTitleSize }) => {
      return (
            <View>
                  <Text
                        style={{
                              fontFamily: FONTS.semibold,
                              fontSize: titleSize,
                              color: COLORS.white,
                        }}
                  >
                        Title
                  </Text>
                  <Text
                        style={{
                              fontFamily: FONTS.regular,
                              fontSize: subTitleSize,
                              color: COLORS.white,
                        }}
                  >
                        Subtitle
                  </Text>
            </View>
      );
};

export const CARDImage = ({ imgURL, index }) => {
      return (
            <Image
                  source={imgURL}
                  resizeMode="contain"
                  style={{
                        width: 48,
                        height: 48,
                        marginLeft: index === 0 ? 0 : -SIZES.font,
                  }}
            />
      );
};


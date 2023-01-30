import React from "react";
import { TouchableOpacity, Text, Image } from "react-native";

import { COLORS, SIZES, FONTS } from "../constants";

export const CircularButton = ({ imgURL, handlePress, ...props }) => {
	return (
		<TouchableOpacity
			style={{
				width: 50,
				height: 50,
				backgroundColor: COLORS.white,
				position: "absolute",
				borderRadius: SIZES.xl,
				alignContent: "center",
				justifyContent: "center",
				...props,
			}}
			onPress={handlePress}
		>
			<Image
				source={imgURL}
				resizeMode="contain"
				style={{ width: 24, height: 24 }}
			/>
		</TouchableOpacity>
	);
};

export const NormalButton = ({ minWidth, fontSize, handlePress, ...props }) => {
	return (
		<TouchableOpacity
			style={{
				minWidth: minWidth,
				backgroundColor: COLORS.secondary,
				borderRadius: SIZES.xl,
				padding: SIZES.small,
				...props,
			}}
			onPress={handlePress}
		>
			<Text
				style={{
					color: COLORS.black,
					fontSize: fontSize,
					fontFamily: FONTS.bold,
					textAlign: "center",
				}}
			>
				Open
			</Text>
		</TouchableOpacity>
	);
};

import React from "react";
import { useNavigation } from "@react-navigation/native";
import { View, Image } from "react-native";

import { COLORS, SIZES } from "../constants";
import { CARDTitle } from "./cardInfo";
import { NormalButton } from "./Button";

const Card = ({ data }) => {
	const navigation = useNavigation();

	return (
		<View
			style={{
				backgroundColor: COLORS.black,
				borderRadius: SIZES.font,
				marginBottom: SIZES.xl,
				margin: SIZES.base,
			}}
		>
			<View
				style={{
					width: "100%",
					height: 250,
				}}
			>
				<Image
					source={data.image}
					resizeMode="cover"
					style={{
						width: "100%",
						height: "100%",
						borderTopLeftRadius: SIZES.font,
						borderTopRightRadius: SIZES.font,
					}}
				/>
			</View>

			<View style={{ padding: SIZES.font, width: "100%" }}>
				<CARDTitle
					title={data.title}
					subTitle={data.subTitle}
					titleSize={SIZES.large}
					subTitleSize={SIZES.small}
				/>
				<View
					style={{
						flexDirection: "row",
						marginTop: SIZES.font,
						justifyContent: "space-between",
						alignItems: "center",
					}}
				>
					<NormalButton
						minWidth={120}
						fontSize={SIZES.font}
						handlePress={() =>
							navigation.navigate(data.title)
						}
					/>
				</View>
			</View>
		</View>
	);
};

export default Card;

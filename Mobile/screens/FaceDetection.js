import React from "react";
import {
	View,
	SafeAreaView,
	FlatList,
	Text,
	StatusBar,
	Image,
	ImageView,
} from "react-native";

import { SIZES, assets } from "../constants";
import { CircularButton, NormalButton, ActiveStatus } from "../components";

const Header = ({ data, navigation }) => {
	<View style={{ width: "100%", height: 375 }}>
		<Image
			source={data.image}
			resizeMode="cover"
			style={{ width: "100%", height: "100%" }}
		/>
		<CircularButton
			imgURL={assets.back}
			handlePress={() => navigation.goBack()}
			left={15}
			top={StatusBar.currentHeight + 15}
		/>
	</View>;
};

const Body = ({ route, navigation }) => {
	const data = route.params;

	return (
		<SafeAreaView style={{ flex: 1 }}>
			<ActiveStatus
				barStyle="dark-content"
				backgroundColor="transparent"
				translucent={true}
			/>
			<View
				style={{
					width: "100%",
					position: "absolute",
					bottom: 0,
					paddingVertical: SIZES.font,
					justifyContent: "center",
					alignItems: "center",
					backgroundColor: "rgba(255, 255, 255, 0.7)",
					zIndex: 1,
				}}
			>
				<NormalButton minWidth={200} fontSize={SIZES.large} />
			</View>
		</SafeAreaView>
	);
};

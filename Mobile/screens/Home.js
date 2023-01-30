import React, { useState } from "react";
import { View, SafeAreaView, FlatList } from "react-native";

import { Card, HomeHeader, ActiveStatus } from "../components";
import { COLORS, cardText } from "../constants";

const Home = () => {
      const [cardData, setCardData] = useState(cardText);

      const handleSearch = (value) => {
        if (value.length === 0) {
          setNftData(cardText);
        }
    
        const filteredData = NFTData.filter((item) =>
          item.name.toLowerCase().includes(value.toLowerCase())
        );
    
        if (filteredData.length === 0) {
          setNftData(cardText);
        } else {
          setNftData(filteredData);
        }
      };

  return (
    <SafeAreaView style={{ flex: 1 }}>
      <ActiveStatus backgroundColor={COLORS.primary} />
      <View style={{ flex: 1 }}>
            <View style={{zIndex: 0}}>
                  <FlatList
                        data={cardText}
                        renderItem={({ item }) => <Card data={item} />}
                        keyExtractor={(item) => item.id}
                        showsVerticalScrollIndicator={false}
                        listHeaderComponent={<HomeHeader onSearch={handleSearch}/>}
                  />
            </View>
        <View
          style={{
            position: "absolute",
            top: 0,
            bottom: 0,
            right: 0,
            left: 0,
            zIndex: -1,
          }}
        >
          <View
            style={{ height: 300, backgroundColor: COLORS.primary }} />
          <View style={{ flex: 1, backgroundColor: COLORS.secondary }} />
        </View>
      </View>
    </SafeAreaView>
  );
};

export default Home;
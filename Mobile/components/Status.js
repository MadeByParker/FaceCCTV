import React from "react";
import { StatusBar } from "react-native";
import { useIsFocused } from "@react-navigation/core";

const ActiveStatus = (props) => {
  const isFocused = useIsFocused();

  return isFocused ? <StatusBar animated={true} {...props} /> : null;
};

export default ActiveStatus;
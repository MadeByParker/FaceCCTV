export const COLORS = {
      primary: "#193dc0",
      secondary: "#62a5e2",

      white: "#ffffff",
      black: "#000000",
      gray: "#74858C",
};

export const SIZES = {
      // global sizes
      base: 8,
      small: 12,
      font: 14,
      medium: 16,
      large: 20,
      xl: 24,
};

export const FONTS = {
      bold: "InterBold",
      semiBold: "InterSemiBold",
      medium: "InterMedium",
      regular: "InterRegular",
      light: "InterLight",
};

export const SHADOWS = {
      light: {
        shadowColor: COLORS.gray,
        shadowOffset: {
          width: 0,
          height: 1,
        },
        shadowOpacity: 0.22,
        shadowRadius: 2.22,
    
        elevation: 3,
      },
      medium: {
        shadowColor: COLORS.gray,
        shadowOffset: {
          width: 0,
          height: 3,
        },
        shadowOpacity: 0.29,
        shadowRadius: 4.65,
    
        elevation: 7,
      },
      dark: {
        shadowColor: COLORS.gray,
        shadowOffset: {
          width: 0,
          height: 7,
        },
        shadowOpacity: 0.41,
        shadowRadius: 9.11,
    
        elevation: 14,
      },
};
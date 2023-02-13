
import { Download, Features, SectionWrapper } from './components';
import assets from './assets';
import styles from './styles/Global';

const App = () => {
  return (
    <>
      <SectionWrapper 
        title="Start Solving Crimes."
        description="FaceCCTV is a facial recognition app that allows users to upload images of people they want to identify. The app then uses deep learning facial detection technology to identify the person in the image, alongside image enhancement technology to improve the quality."
        showBtn
        mockupImg={assets.homeHero}
        banner="banner"
      />
      <SectionWrapper 
        title="Smart User Interface Marketplace"
        description="Experience a buttery UI of ProNef NFT Marketplace. Smooth constant colors of a fluent UI design."
        mockupImg={assets.homeCards}
        reverse
      />
      <Features />
      <SectionWrapper 
        title="Deployment"
        description="FaceCCTV provides cross platform functionality using numerous technologies, React Native and Electron. The app is available on both iOS and Android. The app is also available on the web and desktop."
        mockupImg={assets.feature}
        reverse
      />
      <SectionWrapper 
        title="User Friendly Interface and Experience"
        description="The app was built with a user friendly interface and experience in mind. The app is easy to use and navigate. Along with customisable settings and options are available to the user."
        mockupImg={assets.mockup}
        banner="banner02"
      />
      <Download />
    </>
  );
}

export default App;

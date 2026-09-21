only_modules = {
        "nav.screens.help.params.function":'''
// Pantalla que ENVÍA (HomeScreen)
function HomeScreen({ navigation }) {
  return (
    <Button 
      title="Ir a Perfil"
      onPress={() => navigation.navigate('Profile', { 
        userId: 123, 
        name: 'Juan' 
      })}
    />
  );
}

// Pantalla que RECIBE (ProfileScreen)
function ProfileScreen({ route }) {
  const { userId, name } = route.params;
  return (
    <View>
      <Text>ID: {userId}</Text>
      <Text>Nombre: {name}</Text>
    </View>
  );
}
''',

    "nav.screen.navigation.help.parameters":'''
// Navegar
navigation.navigate('Profile');
navigation.navigate('Profile', { id: 1 });

// Volver
navigation.goBack();

// Reemplazar (sin historial)
navigation.replace('Login');

// Abrir/Cerrar Drawer
navigation.openDrawer();
navigation.closeDrawer();
navigation.toggleDrawer();
''',
    'rn.saveData':'''
import AsyncStorage from '@react-native-async-storage/async-storage';

// 📦 INSTALACIÓN:
// npm install @react-native-async-storage/async-storage
// npx expo install @react-native-async-storage/async-storage

// 1. CREATE - Save data
const saveData = async (key, value) => {
  try {
    await AsyncStorage.setItem(key, JSON.stringify(value));
    return true;
  } catch (error) {
    console.error('Error saving data:', error);
    return false;
  }
};

// 2. READ - Get data
const getData = async (key) => {
  try {
    const value = await AsyncStorage.getItem(key);
    return value != null ? JSON.parse(value) : null;
  } catch (error) {
    console.error('Error reading data:', error);
    return null;
  }
};

// 3. UPDATE - Modify existing data
const updateData = async (key, newValue) => {
  try {
    const exists = await AsyncStorage.getItem(key);
    if (exists === null) return false;
    await AsyncStorage.setItem(key, JSON.stringify(newValue));
    return true;
  } catch (error) {
    console.error('Error updating data:', error);
    return false;
  }
};

// 4. DELETE - Remove specific data
const deleteData = async (key) => {
  try {
    await AsyncStorage.removeItem(key);
    return true;
  } catch (error) {
    console.error('Error deleting data:', error);
    return false;
  }
};

// 5. DELETE ALL - Clear entire storage
const clearAllData = async () => {
  try {
    await AsyncStorage.clear();
    return true;
  } catch (error) {
    console.error('Error clearing data:', error);
    return false;
  }
};

// 6. GET ALL KEYS - Retrieve all keys
const getAllKeys = async () => {
  try {
    return await AsyncStorage.getAllKeys();
  } catch (error) {
    console.error('Error getting keys:', error);
    return [];
  }
};
''',

    # ============================================
    # 📦 STACK NAVIGATION - Navegación por pilas
    # ============================================
    
    "nav.import":'''
import {
    StackNavigation,
    StackScreen,
    BottomTabsNavigation,
    BottomTabScreen,
    DrawerNavigation,
    DrawerScreen,
    TopTabsNavigation,
    TopTabScreen,
    CustomDrawer,
    DrawerItem
} from './components/FletBox'
''',

    "nav.init":'''
import { NavigationContainer } from '@react-navigation/native';
import {
    StackNavigation,
    StackScreen,
    BottomTabsNavigation,
    BottomTabScreen,
    DrawerNavigation,
    DrawerScreen,
    TopTabsNavigation,
    TopTabScreen
} from './components/FletBox';

export default function Main() {
    return (
        <NavigationContainer>
            {/* Tu navegador aquí */}
        </NavigationContainer>
    );
}
''',

    # ============================================
    # STACK NAVIGATION - Ejemplos
    # ============================================

    "nav.stack.init":'''
<StackNavigation
    title="FletBox"
    headerShown={true}
    headerBackgroundColor="#f4511e"
    headerTintColor="#fff"
    components={[
        <StackScreen name="Home" component={HomeScreen} title="Inicio" />,
        <StackScreen name="Profile" component={ProfileScreen} title="Perfil" />,
    ]}
/>
''',

    "nav.stack.onboarding":'''
<StackNavigation
    title="FletBox"
    headerShown={false}
    initialRoute="Welcome"
    components={[
        <StackScreen name="Welcome" component={WelcomeScreen} />,
        <StackScreen name="Login" component={LoginScreen} title="Iniciar sesión" />,
        <StackScreen name="Register" component={RegisterScreen} title="Crear cuenta" />,
        <StackScreen name="Home" component={HomeScreen} title="Inicio" headerShown={true} />
    ]}
/>
''',

    "nav.stack.ecommerce":'''
<StackNavigation
    title="FletBox Shop"
    headerShown={true}
    headerBackgroundColor="#f4511e"
    headerTintColor="#fff"
    headerLeftGlobal={<Icon name="menu" size={24} color="#fff" />}
    headerRightGlobal={<Icon name="cart" size={24} color="#fff" />}
    components={[
        <StackScreen name="Home" component={ProductGridScreen} title="Productos" />,
        <StackScreen name="ProductDetail" component={ProductDetailScreen} title="Detalle" />,
        <StackScreen name="Cart" component={CartScreen} title="Carrito" />,
        <StackScreen name="Checkout" component={CheckoutScreen} title="Finalizar compra" />,
        <StackScreen name="OrderSuccess" component={OrderSuccessScreen} title="¡Gracias!" headerShown={false} />
    ]}
/>
''',

    "nav.stack.auth":'''
<StackNavigation
    title="FletBox"
    headerShown={false}
    components={[
        <StackScreen name="Splash" component={SplashScreen} headerShown={false} />,
        <StackScreen name="Auth" component={AuthScreen} headerShown={false} />,
        <StackScreen name="Main" component={MainApp} headerShown={false} />,
    ]}
/>
''',

    # ============================================
    # BOTTOM TABS NAVIGATION - Navegación inferior
    # ============================================

    "nav.bottomtabs.init":'''
<BottomTabsNavigation
    activeTintColor="#f4511e"
    inactiveTintColor="#fff"
    tabBarStyle={{ backgroundColor: '#1e293b', borderTopColor: 'yellow' }}
    components={[
        <BottomTabScreen name="Home" title="Inicio" icon="home" component={HomeScreen} />,
        <BottomTabScreen name="Search" title="Buscar" icon="search" component={SearchScreen} />,
        <BottomTabScreen name="Profile" title="Perfil" icon="person" component={ProfileScreen} />,
    ]}
/>
''',

    "nav.bottomtabs.social":'''
<BottomTabsNavigation
    activeTintColor="#f4511e"
    inactiveTintColor="#fff"
    tabBarStyle={{ backgroundColor: '#1e293b', elevation: 8 }}
    components={[
        <BottomTabScreen 
            name="Feed" 
            title="Feed" 
            icon="home" 
            component={FeedScreen}
            tabBarBadge={notifications.length}
            tabBarBadgeStyle={{ backgroundColor: 'red' }}
        />,
        <BottomTabScreen 
            name="Explore" 
            title="Explorar" 
            icon="compass" 
            component={ExploreScreen}
        />,
        <BottomTabScreen 
            name="Messages" 
            title="Mensajes" 
            icon="chatbubbles" 
            component={MessagesScreen}
            tabBarBadge={unreadCount}
        />,
        <BottomTabScreen 
            name="Profile" 
            title="Perfil" 
            icon="person" 
            component={ProfileScreen}
        />,
    ]}
/>
''',

    "nav.bottomtabs.ecommerce":'''
<BottomTabsNavigation
    activeTintColor="#f4511e"
    inactiveTintColor="#fff"
    tabBarStyle={{ backgroundColor: '#1e293b' }}
    components={[
        <BottomTabScreen name="Shop" title="Tienda" icon="storefront" component={ShopScreen} />,
        <BottomTabScreen name="Categories" title="Categorías" icon="grid" component={CategoriesScreen} />,
        <BottomTabScreen 
            name="Cart" 
            title="Carrito" 
            icon="cart" 
            component={CartScreen}
            tabBarBadge={cartItems.length}
        />,
        <BottomTabScreen name="Favorites" title="Favoritos" icon="heart" component={FavoritesScreen} />,
        <BottomTabScreen name="Profile" title="Mi Cuenta" icon="person" component={ProfileScreen} />,
    ]}
/>
''',

    # ============================================
    # TOP TABS NAVIGATION - Pestañas superiores
    # ============================================

    "nav.toptabs.init":'''
<TopTabsNavigation
    activeTintColor="#f4511e"
    inactiveTintColor="#999"
    indicatorColor="#f4511e"
    tabBarStyle={{ backgroundColor: '#fff' }}
    components={[
        <TopTabScreen name="ForYou" title="Para ti" component={ForYouScreen} />,
        <TopTabScreen name="Following" title="Siguiendo" component={FollowingScreen} />,
        <TopTabScreen name="Trending" title="Tendencias" component={TrendingScreen} />,
    ]}
/>
''',

    "nav.toptabs.product":'''
<TopTabsNavigation
    activeTintColor="#f4511e"
    inactiveTintColor="#999"
    indicatorColor="#f4511e"
    tabBarStyle={{ backgroundColor: '#fff' }}
    components={[
        <TopTabScreen name="Details" title="Detalles" component={ProductDetailsScreen} />,
        <TopTabScreen name="Reviews" title={`Reseñas (${reviews.length})`} component={ProductReviewsScreen} />,
        <TopTabScreen name="Specs" title="Especificaciones" component={ProductSpecsScreen} />,
    ]}
/>
''',

    "nav.toptabs.profile":'''
<TopTabsNavigation
    activeTintColor="#f4511e"
    inactiveTintColor="#999"
    indicatorColor="#f4511e"
    components={[
        <TopTabScreen name="Posts" title="Publicaciones" component={UserPostsScreen} />,
        <TopTabScreen name="Reels" title="Reels" component={UserReelsScreen} />,
        <TopTabScreen name="Saved" title="Guardados" component={UserSavedScreen} />,
        <TopTabScreen name="Tags" title="Etiquetas" component={UserTagsScreen} />,
    ]}
/>
''',

    # ============================================
    # DRAWER NAVIGATION - Menú lateral
    # ============================================

    "nav.drawer.init":'''
<DrawerNavigation
    headerShown={true}
    headerBackgroundColor="#f4511e"
    headerLeft={<Icon name="menu" size={24} color="#fff" />}
    drawerStyle={{ width: 280, backgroundColor: '#fff' }}
    components={[
        <DrawerScreen name="Home" title="Inicio" icon="home" component={HomeScreen} />,
        <DrawerScreen name="Profile" title="Perfil" icon="person" component={ProfileScreen} />,
        <DrawerScreen name="Settings" title="Configuración" icon="settings" component={SettingsScreen} />,
    ]}
/>
''',

    "nav.drawer.profile":'''
<DrawerNavigation
    headerShown={true}
    headerBackgroundColor="#f4511e"
    headerLeft={<Icon name="menu" size={24} color="#fff" />}
    headerRight={<Icon name="search" size={24} color="#fff" />}
    drawerStyle={{ width: 280, backgroundColor: '#fff' }}
    drawer={MyDrawer}
    components={[
        <DrawerScreen name="Home" component={HomeScreen} />,
        <DrawerScreen name="Stats" component={StatsScreen} />,
        <DrawerScreen name="Orders" component={OrdersScreen} />,
        <DrawerScreen name="Wishlist" component={WishlistScreen} />,
        <DrawerScreen name="Settings" component={SettingsScreen} />,
    ]}
/>
''',

    # ============================================
    # CUSTOM DRAWER - Menú lateral personalizado
    # ============================================

    "nav.customdrawer.init":'''
<CustomDrawer
    header={
        <Container padding={20} bgcolor="#f4511e" alignItems="center">
            <Avatar label="FB" size={60} bgcolor="#fff" color="#f4511e" />
            <Text label="FletBox Pro" color="white" size={18} weight="bold" marginTop={8} />
            <Text label="Crea apps increíbles" color="rgba(255,255,255,0.8)" size={12} />
        </Container>
    }
    components={[
        <DrawerItem name="Home" label="Inicio" icon="home" onPress={() => {}} />,
        <DrawerItem name="Explore" label="Explorar" icon="compass" onPress={() => {}} />,
        <DrawerItem name="Library" label="Biblioteca" icon="library" onPress={() => {}} />,
    ]}
    footer={
        <Container padding={16}>
            <DrawerItem name="Settings" label="Configuración" icon="settings" onPress={() => {}} />
            <DrawerItem name="Help" label="Ayuda" icon="help-circle" onPress={() => {}} />
        </Container>
    }
/>
''',

    "nav.customdrawer.user":'''
<CustomDrawer
    header={
        <GestureDetector on_tap={() => navigation.navigate('Profile')}>
            <Container direction="row" alignItems="center" padding={16} bgcolor="#f0f0f0">
                <Avatar source={user.avatar} size={55} />
                <Container marginLeft={12} expand={true}>
                    <Text label={user.name} size={16} weight="bold" />
                    <Text label={user.email} size={12} color="#666" />
                </Container>
                <Icon name="chevron-forward" size={20} color="#666" />
            </Container>
        </GestureDetector>
    }
    components={[
        <DrawerItem name="Dashboard" label="Dashboard" icon="speedometer" onPress={() => {}} />,
        <DrawerItem name="Projects" label="Proyectos" icon="folder" onPress={() => {}} badge="12" />,
        <DrawerItem name="Tasks" label="Tareas" icon="checkbox" onPress={() => {}} badge="5" badgeColor="red" />,
        <DrawerItem name="Messages" label="Mensajes" icon="chatbubbles" onPress={() => {}} badge="3" />,
    ]}
    footer={
        <Container padding={16}>
            <DrawerItem name="Settings" label="Configuración" icon="settings" onPress={() => {}} />
            <Divider marginVertical={8} />
            <DrawerItem name="Logout" label="Cerrar sesión" icon="log-out" iconColor="red" labelColor="red" onPress={handleLogout} />
        </Container>
    }
/>
''',

    # ============================================
    # FLETBOX NAVIGATION - Navegadores personalizados
    # ============================================

    "fb.nav.stack.init":'''
<StackNavigation
    title="FletBox"
    headerShown={true}
    headerBackgroundColor="#f4511e"
    headerTintColor="#fff"
    components={[
        <StackScreen name="Home" component={HomeScreen} title="Inicio" />,
        <StackScreen name="Profile" component={ProfileScreen} title="Perfil" />,
    ]}
/>
''',

    "fb.nav.bottomtabs.init":'''
<BottomTabsNavigation
    activeTintColor="#f4511e"
    inactiveTintColor="#fff"
    tabBarStyle={{ backgroundColor: '#1e293b', borderTopColor: 'yellow' }}
    components={[
        <BottomTabScreen name="Home" title="Inicio" icon="home" component={HomeScreen} />,
        <BottomTabScreen name="Profile" title="Perfil" icon="person" component={ProfileScreen} />,
    ]}
/>
''',

    "fb.nav.toptabs.init":'''
<TopTabsNavigation
    activeTintColor="#f4511e"
    inactiveTintColor="#999"
    indicatorColor="#f4511e"
    components={[
        <TopTabScreen name="Feed" title="Feed" component={FeedScreen} />,
        <TopTabScreen name="Explore" title="Explorar" component={ExploreScreen} />,
    ]}
/>
''',

    "fb.nav.drawer.init":'''
<DrawerNavigation
    headerShown={false}
    drawerStyle={{ width: 280, backgroundColor: '#1e293b' }}
    components={[
        <DrawerScreen name="Home" title="Inicio" icon="home" component={HomeScreen} />,
        <DrawerScreen name="Profile" title="Perfil" icon="person" component={ProfileScreen} />,
    ]}
/>
''',

    "fb.nav.customdrawer.init":'''
<CustomDrawer
    header={
        <View style={{ padding: 20, alignItems: 'center' }}>
            <Avatar label="FB" size={60} bgcolor="#fff" color="#f4511e" />
            <Text label="FletBox Pro" color="white" size={18} weight="bold" />
        </View>
    }
    components={[
        <DrawerItem name="Home" label="Inicio" icon="home" onPress={() => {}} />,
        <DrawerItem name="Explore" label="Explorar" icon="compass" onPress={() => {}} />,
    ]}
    footer={
        <View style={{ padding: 16 }}>
            <DrawerItem name="Settings" label="Configuración" icon="settings" onPress={() => {}} />
        </View>
    }
/>
''',

    # ============================================
    # PARÁMETROS Y OPCIONES
    # ============================================

    "nav.stack.params":'''
initialRouteName="Home"              // string - primera pantalla
presentation="card"                  // 'card' | 'modal' | 'transparentModal'
animation="slide_from_right"         // 'slide_from_right' | 'fade' | 'none'
animationDuration={300}              // number - duración en ms
gestureDirection="horizontal"        // 'horizontal' | 'vertical'
gestureEnabled={true}                // boolean - gestos de deslizamiento
gestureResponseDistance={50}         // number - píxeles desde el borde
keyboardHandlingEnabled={true}       // boolean - manejo del teclado
detachInactiveScreens={true}         // boolean - optimización de memoria
''',

    "nav.stack.options.screenOptions":'''
// HEADER OPTIONS
headerShown={true}                   // boolean - mostrar/ocultar header
headerStyle={{ backgroundColor: '#f4511e' }}  // object - estilo del header
headerTintColor="#fff"               // string - color del texto
headerTitleStyle={{ fontWeight: 'bold', fontSize: 24 }}  // object - estilo del título
headerTitleAlign="center"            // 'center' | 'left' - alineación del título
headerLeft={() => <Icon name="menu" size={24} color="#fff" />}  // function - icono izquierdo
headerRight={() => <Icon name="search" size={24} color="#fff" />} // function - icono derecho
headerBackVisible={true}             // boolean - mostrar botón de atrás
headerBackTitle="Atrás"              // string - texto del botón de atrás
headerTransparent={false}            // boolean - header transparente
headerShadowVisible={true}           // boolean - mostrar sombra

// TAB BAR OPTIONS (para BottomTabs)
tabBarStyle={{ backgroundColor: '#fff', height: 60 }}  // object - estilo de la barra
tabBarActiveTintColor="#f4511e"      // string - color del tab activo
tabBarInactiveTintColor="#999"       // string - color del tab inactivo
tabBarLabelStyle={{ fontWeight: 'bold' }}  // object - estilo de la etiqueta
tabBarShowLabel={true}               // boolean - mostrar etiquetas
tabBarShowIcon={true}                // boolean - mostrar iconos
tabBarBadge={3}                      // number | string - badge en el tab
tabBarBadgeStyle={{ backgroundColor: 'red' }}  // object - estilo del badge

// DRAWER OPTIONS
drawerStyle={{ width: 280, backgroundColor: '#fff' }}  // object - estilo del drawer
drawerPosition="left"                // 'left' | 'right' - posición del drawer
drawerType="front"                   // 'front' | 'back' | 'slide'
drawerActiveTintColor="#f4511e"      // string - color del item activo
drawerInactiveTintColor="#999"       // string - color del item inactivo
drawerActiveBackgroundColor="rgba(244,81,30,0.1)"  // string - fondo del item activo

// TOP TABS OPTIONS
tabBarIndicatorStyle={{ backgroundColor: '#f4511e', height: 3 }}  // object - estilo del indicador
swipeEnabled={true}                  // boolean - permitir deslizamiento
animationEnabled={true}              // boolean - animación al cambiar de tab
lazy={true}                          // boolean - carga perezosa
''',

    # ============================================
    # CUSTOM DRAWER PRÁCTICO
    # ============================================

    "nav.customDrawer.made":'''
function MyDrawer({ navigation }) {
    const [darkMode, setDarkMode] = useState(false);
    const [activeItem, setActiveItem] = useState('home');

    return (
        <CustomDrawer
            header={
                <Container
                    bgimage={require('../assets/icon.png')}
                    bgimageStyle={{ resizeMode: 'repeat', opacity: 0.3 }}
                    height={200}
                    alignItems="flex-end"
                    justifyContent="flex-end"
                    padding={16}
                >
                    <Image source={require('./assets/icon.png')} width={50} height={50} circular={true} />
                    <Text label="Javier Quesada" color="#fff" size={18} weight="bold" />
                    <Text label="kuko53348@gmail.com" color="#94a3b8" size={12} />
                </Container>
            }
            components={[
                <DrawerItem 
                    key="home"
                    name="home"
                    label="Inicio"
                    icon="home"
                    onPress={() => {
                        setActiveItem('home');
                        navigation.navigate('Home');
                    }}
                />,
                <DrawerItem 
                    key="profile"
                    name="profile"
                    label="Perfil"
                    icon="person"
                    onPress={() => {
                        setActiveItem('profile');
                        navigation.navigate('Profile');
                    }}
                />,
                <DrawerItem 
                    key="settings"
                    name="settings"
                    label="Configuración"
                    icon="settings"
                    onPress={() => {
                        setActiveItem('settings');
                        navigation.navigate('Settings');
                    }}
                />,
            ]}
            footer={
                <Container borderTopWidth={1} borderTopColor="#334155" padding={16}>
                    <Button 
                        variant="elevated"
                        label="Cerrar sesión"
                        color="#f87171"
                        iconColor="#f87171"
                        icon="log-out"
                        on_click={() => navigation.navigate('Login')}
                    />
                    <Text label="Versión 1.0.0" color="#666" fontSize={10} textAlign="center" />
                </Container>
            }
            activeItem={activeItem}
            onItemPress={(item) => console.log('Item presionado:', item.label)}
        />
    );
}
''',
}

only_controls = {
        'fb.useRef.animation':'''
const valor = useRef(new Animated.Value(0)).current; 
// const nuevoValor = valor._value === 0 ? 1 : 0;
''',
        'fb.interpolate':'''
const valor = useRef(new Animated.Value(0)).current; 

// const nuevoValor = valor._value === 0 ? 1 : 0;
const rotacionFrontal = valor.interpolate({
    inputRange: [0, 1],
    outputRange: ['0deg', '180deg'],
});
''',
        'fb.useEffect':'''
  useEffect(() => {
    Animated.timing(rotateValue, {
      toValue: 360,
      duration: 1000,
      usenativeDriver: true
    }).start();
  }, []);
''',
    'fb.animated.useRef':'''
  const rotateValue = useRef(new Animated.Value(0)).current;
  // const nuevoValor = valor._value === 0 ? 1 : 0;
''',
    'fb.animated.scrollEvent':'''
const ScrollExample = () => {
  const scrollY = useRef(new Animated.Value(0)).current;

  const inputRange = [0, 200];
  const outputRange = [1, 0];
  const opacity = scrollY.interpolate({ 
    inputRange, 
    outputRange 
  });

  return (
    <Animated.ScrollView
      onScroll={Animated.event(
        [{ nativeEvent: { contentOffset: { y: scrollY , } } }],
        { useNativeDriver: true }
      )}
      scrollEventThrottle={16}
    >
      <Animated.View style={{ height: 300, backgroundColor: 'purple', opacity }}>
        <Text>Header con fade al hacer scroll</Text>
      </Animated.View>
      {[...Array(20)].map((_, i) => (
        <View key={i} style={{ height: 80, margin: 10, backgroundColor: '#ddd' }} />
      ))}
    </Animated.ScrollView>
  );
};
''',
'fb.array.init': '''
      {
      [...Array(20)].map((_, i) => (
        <View key={i} style={{ height: 80, margin: 10, backgroundColor: '#ddd' }} />
      ))
      }
''',
        'fb.animated.init':'''
import { Animated, useRef, useEffect } from 'react';

const MyComponent = () => {
  // ✅ FORMA CORRECTA
  const rotateValue = useRef(new Animated.Value(0)).current;
  const scaleValue = useRef(new Animated.Value(1)).current;
  const opacityValue = useRef(new Animated.Value(1)).current;

  // run first time automaticly
  useeffect(() => {
    animated.timing(rotatevalue, {
      tovalue: 360,
      duration: 1000,
      usenativedriver: true
    }).start();
  }, []);

  // run as function
  const runEffect = () => {
    // const nuevoValor = rotateValue._value === 0 ? 1 : 0;
    animated.timing(rotatevalue, {
      tovalue: 360,
      duration: 1000,
      usenativedriver: true
    }).start();
  };

  return (
    <Animated.View
      style={{
        transform: [
          { rotate: rotateValue },
          { scale: scaleValue }
        ],
        opacity: opacityValue
      }}
    />
  );
};
''',
    'fb.animatedListView':'''
<AnimatedListView
  key="demo"
  data={data}

  // --- vertical
  snapToInterval={height}
  contentContainerStyle={{
      // paddingTop: height/4, paddingBottom: height/4, 
      paddingBottom: 46 ,
  }}
  showsVerticalScrollIndicator={false}

  // --- horizontal
  // horizontal={true}
  // snapToInterval={width}
  // showsHorizontalcrollIndicator={false}

  // pagingEnabled={true} // or snapToInterval
  snapToAlignment="start" // center start end
  decelerationRate="fast" // fast normal slow
  scrollEventThrottle={16}

  // ListFooterComponent={null}
  // contentInset={{ bottom: 0 }}
  // getItemLayout={(data, index) => ({
  //   length: height,
  //   offset: height * index,
  //   index,
  // })}

  // ----- manually mode  put down fuction => ()
  // const scrollX = useRef(new Animated.Value(0)).current;
  
  // onScroll={Animated.event(
  //   [{ nativeEvent: { contentOffset: { x: scrollX } } }],
  //   { useNativeDriver: true }
  // )}

  keyExtractor={(item, index) => index.toString()}

  renderItem={({ item, index, scrollX, scrollY }) => {
    // ----- manually mode
    // const inputRange = [
    //   (index - 1) * height,
    //   index * height,
    //   (index + 1) * height
    // ];

    // const scale = scrollY.interpolate({
    //   inputRange,
    //   outputRange: [0.2, 1, 0.2],
    //   extrapolate: 'clamp'
    // });

    const animatedStyle = combineScrollEffects(
      [
        // { effect: 'spotlight', outputRange: [0.85, 1.1, 0.85] },  // escala
        // { effect: 'appleCard', outputRange: [0.92, 1, 0.92] },   // escala
        // { effect: 'netflix', outputRange: [0.9, 1.05, 0.9] },    // escala
        { effect: 'spotify', outputRange: [0.9, 1.1, 0.9] },     // escala
        // { effect: 'scale', outputRange: [0.1, 1, 0.1] },
        // { effect: 'fade', outputRange: [0.1, 1, 0.1] },
        // { effect: 'parallax', outputRange: [30, 0, -30] },
        { effect: 'rotateY', outputRange: ['180deg', '0deg', '-180deg'] },
      ],
      { scroll: scrollY, index, itemSize: height }
    );

    return (
        <AnimatedBox 
            animatedStyle={ animatedStyle }
            child={<Text label='Flet-box' />
            }/>
    )}
  }
/>
''',
    'fb.animated.view.init':'''

    <Animated.View
      style={{
        opacity,
        backgroundColor,
        width, hight,
        margin, padding,
        borderRadius,
        transform: [
          { rotate: rotateValue },
          { rotateX: rotateValueX },
          { rotateY: rotateValueY },
          { translateX: translateX },
          { translateY: translateY },
          { scale: scaleValue }
        ],
        // backfaceVisibility: 'hidden',
        // justifyContent: 'center',
        // position: 'absolute',
        // alignItems: 'center',
        // shadowColor: '#000',
        // shadowOffset: { width: 0, height: 2 },
        // shadowOpacity: 0.3,
        // shadowRadius: 4,
        // elevation: 5,
      }}
    />
''',
        'fb.animatedBox.db':'''
import { AnimatedBox, getAnimation } from '../components/FletBox';

export const AnimatedBoxExample = () => {
  const fadeIn = getAnimation('fadeIn');
  const bounceIn = getAnimation('bounceIn');
  const pulse = getAnimation('pulse');
  const spin = getAnimation('spin');

  const allAnimations = [
    ..fadein, ...bounceIn, ...pulse, ...spin
  ]

  return (
    <AnimatedBox
      animations={fadeIn.code}
      child={
        <Text label="Fade In" />
      }
    />
  );
};
''',
        'fb.animatedBox.db.all':'''
// 1. ENTRADAS
// fadeIn, fadeUp, fadeDown, fadeLeft, fadeRight
// slideInRight, slideInLeft, slideInTop, slideInBottom
// zoomIn, zoomOut, pop, bounceIn, swingIn, rotateIn, flipIn

// 2. SALIDAS
// fadeOut, slideOutRight, slideOutLeft, slideOutTop, slideOutBottom
// zoomOut, bounceOut, flipOut

// 3. LOOPS (infinitos)
// spin, slowSpin, fastSpin, pulse, heartbeat, float, wave, breathe

// 4. ATENCIÓN
// shake, wobble, flash, highlight, rumble

// 5. AVANZADOS
// bounce, confetti, doorOpen, doorClose, tilt, stretch, compress, elasticBand, backEffect

// 6. TRANSICIONES
// slideTransition, fadeTransition, zoomTransition, crossfade
''',
        'fb.animatedBox.init': '''
<AnimatedBox
  // const scrollY = useRef(new Animated.Value(0)).current;
  // const AnimatedScrollView = Animated.createAnimatedComponent(ScrollView);

  // animatedStyle={{ 
  //   transform: [{
  //     translateY: scrollY.interpolate({
  //       inputRange: [-200, 0, 200],
  //       outputRange: [-100, 0, 100],
  //       extrapolate: 'clamp'
  //     })
  //   }],
  //   opacity: scrollY.interpolate({
  //     inputRange: [0, 150],
  //     outputRange: [1, 0.5],
  //     extrapolate: 'clamp'
  //   })
  // }}
  // style={{ width: width, height: 300, backgroundColor: '#e74c3c', justifyContent: 'center', alignItems: 'center', }}

  animations={[
    { type: "timing", effect: "opacity", from: 0, to: 1, duration: 500, loop: true, iterations: 3 },
    { type: "spring", effect: "scale", from: 0.5, to: 1, friction: 4, tension: 120, loop: true, iterations: 3 },
    { type: "decay", effect: "translateX", from: 0, to: 340, velocity: 2, deceleration: 0.99, loop: true, iterations: 3 }
  ]}
  animationGroup="parallel" // sequence stagger
  child={<Text label="Animación completa - 3 loops" />}
/>
''',
        'fb.animatedBox.basic':'''
<AnimatedBox
  index={0}
  // style={{ width: width, height: 300, backgroundColor: '#e74c3c', justifyContent: 'center', alignItems: 'center', }}
  animations={[
    { type: "timing", effect: "opacity", from: 0, to: 1, duration: 500 }
  ]}
  animationGroup="parallel"
  child={<Text label="Hola" />}
/>
''',
        'fb.animatedBox.full':'''
<AnimatedBox
  // animatedStyle={{ 
  //   translate[Y,X], rotate, rotate[Y,X], scale
  //   transform: [{
  //     translateY: scrollY.interpolate({
  //       inputRange: [-200, 0, 200],
  //       outputRange: [-100, 0, 100],
  //       extrapolate: 'clamp'
  //     })
  //   }],
  //  opacity, scale, 
  //   opacity: scrollY.interpolate({
  //     inputRange: [0, 150],
  //     outputRange: [1, 0.5],
  //     extrapolate: 'clamp'
  //   })
  // }}
  animations={[
    // type: timing , spring , decay
    // effect: opacity , scale , translateX , translateY , rotate
    // numTimes loop iterations
    { type: "spring", effect: "scale", 
      from: 0.5, to: 1, friction: 4, tension: 120, 
      loop: true, iterations: 3 },
    
    { type: "decay", effect: "translateX",
      velocity: 2, deceleration: 0.99, 
      loop: true, iterations: 3 },
    
    { type: "timing", effect: "rotate", 
      from: 0, to: 360, duration: 1000, 
      loop: true, iterations: 3 },

    { type: "timing", effect: "translateY", 
      from: -50, to: 0, duration: 500, 
      loop: true, iterations: 3 }
  ]}
  
  // ========== TIPOS DE GRUPO ==========
  // parallel , sequence , stagger
  animationGroup="parallel"
  
  child={<Text label="Múltiples animaciones - 3 loops" />}
/>
''',
'fb.animateBox.animation':'''
// type: timing , spring , decay
// effect: opacity , scale , translateX , translateY , rotate
// numTimes loop iterations
{ type: "spring", effect: "scale", 
  from: 0.5, to: 1, friction: 4, tension: 120, 
  loop: true, iterations: 3 },

{ type: "decay", effect: "translateX",
  velocity: 2, deceleration: 0.99, 
  loop: true, iterations: 3 },

{ type: "timing", effect: "rotate", 
  from: 0, to: 360, duration: 1000, 
  loop: true, iterations: 3 },

{ type: "timing", effect: "translateY", 
  from: -50, to: 0, duration: 500, 
  loop: true, iterations: 3 }
''',
        'fb.navigation.params.routes':'''
{ navigation, route }
''',
        'fb.navigation.goTo':'''
// const { id, params } = route.params || {};
// navigation.navigate('Profile');
// on_click={()=> goTo(navigation, 'Profile', {'id': 'myId'}); }
''',
        'fb.json':'''
JSON.stringify(dataObject);
''',
        'fb.database':'''
const database = {
    'demo': 'flet-box database',
};

const getItem = (item) => {
  if (!item) return undefined;
  
  const items = {
    'noFound': `No exist ${item} in database!!`,
    ...database,
  };
  
  return items[item] || items.noFound;
};
''',
        'fb.scrollCapture':'''
  const scrollY = useRef(new Animated.Value(0)).current;
  const scrollX = useRef(new Animated.Value(0)).current;

  // Si viene onScroll por props, usarlo; si no, usar el interno
  const handleScroll = onScroll || Animated.event(
    [{ nativeEvent: { contentOffset: { x: scrollX, y: scrollY } } }],
    { useNativeDriver: true }
  );

  onScroll={handleScroll}  // ← Usar el que corresponda
''',
        'fb.animated.flatList.full':'''
const flatListRef = useRef(null);
const scrollY = useRef(new Animated.Value(0)).current;

<Animated.FlatList
  // ref={flatListRef}
  // ItemSeparatorComponent={() => <Divider />}
  data={data}
  keyExtractor={(item) => item.id}
  renderItem={({ item , index }) => 
    <Item />
   }

  contentContainerStyle={{ 
    opacity,
    backgroundColor,
    width, hight,
    margin, padding,
    borderRadius,
    transform: [
      { rotate: rotateValue },
      { rotateX: rotateValueX },
      { rotateY: rotateValueY },
      { translateX: translateX },
      { translateY: translateY },
      { scale: scaleValue }
    ],
    // backfaceVisibility: 'hidden',
    // justifyContent: 'center',
    // position: 'absolute',
    // alignItems: 'center',
    // shadowColor: '#000',
    // shadowOffset: { width: 0, height: 2 },
    // shadowOpacity: 0.3,
    // shadowRadius: 4,
    // elevation: 5,
  }}

  scrollEventThrottle={16}

  paginEnabled={true}
  horizontal={false}
  showsVerticalScrollIndicator={true}

  // necessary
  onScroll={Animated.event(
    // vertical
    [{ nativeEvent: { contentOffset: { x: scrollX } } }],
    // horizontal
    // [{ nativeEvent: { contentOffset: { y: scrollY } } }],
    { useNativeDriver: true }
  )}

  // initialNumToRender={10}
  // maxToRenderPerBatch={10}
  // removeClippedSubviews={true}
  // initialNumToRender={10}
  // onEndReached={cargarMas}
  // onRefresh={recargar}
  // refreshing={refreshing}
  // ListHeaderComponent={<Header />}
  // ListEmptyComponent={<Empty />}
  // maxToRenderPerBatch={10}
  // removeClippedSubviews={true}
/>
''',
        'fb.animation.interpolate.help':'''
// 🔥 PARALLEL (basado en TIEMPO)
Animated.parallel([
  Animated.timing(opacity, { toValue: 0, duration: 1000 }),
  Animated.timing(scale, { toValue: 0.5, duration: 1000 }),
  Animated.timing(translateY, { toValue: -50, duration: 1000 }),
]).start();
// → Todo cambia al mismo tiempo DURANTE 1 segundo

// 🔥 INTERPOLATE (basado en SCROLL)
const opacity = scrollY.interpolate({...});     // ← cambia con scroll
const scale = scrollY.interpolate({...});       // ← cambia con scroll
const translateY = scrollY.interpolate({...});  // ← cambia con scroll
// → Todo cambia al mismo tiempo CUANDO scrolleas
''',
        'fb.animated.stagger':'''
const valor = useRef(new Animated.Value(0)).current;

const animacionCompleta = () => {
    // setValue(!value)
    // const value = demo._value === 1 ? 0 : 1;
    Animated.stagger(
    100, // delay
    [
      Animated.timing(opacidad, { toValue: 1, duration: 1000, useNativeDriver: true }),
      Animated.timing(mover, { toValue: 150, duration: 1000, useNativeDriver: true }),
      Animated.timing(escala, { toValue: 1.3, duration: 1000, useNativeDriver: true }),
    ]).start();
    };
''',
        'fb.animated.sequence':'''
const valor = useRef(new Animated.Value(0)).current;

const animacionCompleta = () => {
    // setValue(!value)
    // const value = demo._value === 1 ? 0 : 1;
    Animated.sequence([     // ← todas al mismo tiempo
      Animated.timing(opacidad, { toValue: 1, duration: 1000, useNativeDriver: true }),
      Animated.timing(mover, { toValue: 150, duration: 1000, useNativeDriver: true }),
      Animated.timing(escala, { toValue: 1.3, duration: 1000, useNativeDriver: true }),
    ]).start();
    };
''',
        'fb.animated.loop':'''
Animated.loop(
  Animated.sequence([
    Animated.timing(...),
    Animated.timing(...)
  ])
)
''',
        'fb.animated.parallel':'''
const demo = useRef(new Animated.Value(0)).current;

const animacionCompleta = () => {
    // const value = demo._value === 1 ? 0 : 1;
    Animated.parallel([     // ← todas al mismo tiempo
      Animated.timing(opacidad, { toValue: 1, duration: 1000, useNativeDriver: true }),
      Animated.timing(mover, { toValue: 150, duration: 1000, useNativeDriver: true }),
      Animated.timing(escala, { toValue: 1.3, duration: 1000, useNativeDriver: true }),
    ]).start();
    };
''',
        'fb.animated.imports':'''
// import React, { useState , useRef} from 'react';
// import { View , Animated} from 'react-native';
const [ value, setValue ] = useState('red');
const demo = useRef(new Animated.Value(1)).current;
// setValue(!value)
''',
        'fb.animated.interpolate':'''
const demo = useRef(new Animated.Value(0)).current;
// const value = demo._value === 1 ? 0 : 1;
// setValue(!value)

const rotate = demo.interpolate({
    inputRange: [0,1],
    outputRange: ['100deg','0deg']
});

''',
        'fb.animated.spring.':'''
const demo = useRef(new Animated.Value(0)).current;
// const value = demo._value === 1 ? 0 : 1;
// setValue(!value)

// inside useEffect or fuction
Animated.spring(
    // setValue(!value)
    // width, height, backgroundColor
    // margin, padding, borderRadius
    opacity: opacity
    { 
        toValue: 100, 
        friction: 2, 
        tension: 40, 
        useNativeDriver: true 
    }
).start();
''',
        'fb.animated.timing.':'''
const demo = useRef(new Animated.Value(0)).current;
// const value = demo._value === 1 ? 0 : 1;
// setValue(!value)

// inside useEffect or fuction
Animated.timing(
    // width, height, backgroundColor
    // margin, padding, borderRadius
    opacity: opacity
    { 
        toValue: 1, 
        duration: 500, 
        useNativeDriver: true 
    }
).start();
''',
        'fb.animated.decay.':'''
const demo = useRef(new Animated.Value(0)).current;
// const value = demo._value === 1 ? 0 : 1;

// inside useEffect or fuction
Animated.decay(
    // width, height, backgroundColor
    // margin, padding, borderRadius
    opacity: opacity
    { 
        toValue: 1, 
        friction: 2,
        velocity: 0.5, 
        deceleration: 0.599,
        useNativeDriver: true 
    }
).start();
''',
        'fb.animated.variable':'''
const valor = useRef(new Animated.Value(0)).current;
// const value = demo._value === 1 ? 0 : 1;

// 3 valores: agranda y vuelve
const escala = valor.interpolate({
    inputRange: [0, 0.5, 1],
    outputRange: [1, 1.8, 1]
});

''',
        'fb.animated.style':'''
<Animated.View
  style={{
    // Estilos NORMALES (sin transform)
    width: 100,
    height: 100,
    backgroundColor: colorAnimado,
    borderRadius: 10,
    opacity: valorOpacidad,
    
    // Estilos de TRANSFORM (dentro del array)
    transform: [
          { translateX: moverX },
          { translateY: moverY },
          { scale: escala },
          { rotate: rotacion }
        ]
      }}
    />

    {/* component inside */}

</Animated.view>
''',
        'fb.animated.interpolate.exemple':'''
import React, { useRef } from 'react';
import { View, Text, TouchableOpacity, Animated } from 'react-native';

const App = () => {
  const valor = useRef(new Animated.Value(0)).current;

  // 3 valores: agranda y vuelve
  const escala = valor.interpolate({
    inputRange: [0, 0.5, 1],
    outputRange: [1, 1.8, 1]
  });

  // 4 valores: gira por etapas
  const rotacion = valor.interpolate({
    inputRange: [0, 0.3, 0.6, 1],
    outputRange: ['0deg', '120deg', '240deg', '360deg']
  });

  // 5 valores: va, vuelve, va atrás, vuelve
  const moverX = valor.interpolate({
    inputRange: [0, 0.25, 0.5, 0.75, 1],
    outputRange: [0, 80, 0, -80, 0]
  });

  const iniciar = () => {
    valor.setValue(0);
    Animated.timing(valor, {
      toValue: 1,
      duration: 2000,
      useNativeDriver: true,
    }).start();
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      
      <Animated.View
        style={{
          width: 80,
          height: 80,
          backgroundColor: 'red',
          transform: [
            { translateX: moverX },
            { rotate: rotacion },
            { scale: escala }
          ]
        }}
      />

      <TouchableOpacity onPress={iniciar} style={{ marginTop: 100 }}>
        <Text style={{ backgroundColor: 'blue', color: 'white', padding: 10 }}>
          ANIMAR
        </Text>
      </TouchableOpacity>

      <View style={{ marginTop: 50 }}>
        <Text>Scale: 3 valores [1, 1.8, 1]</Text>
        <Text>Rotate: 4 valores [0,120,240,360]°</Text>
        <Text>TranslateX: 5 valores [0,80,0,-80,0]</Text>
      </View>

    </View>
  );
};

export default App;
''',
        'fb.animated.parallel.exemple':'''
import React, { useRef } from 'react';
import { View, Text, TouchableOpacity, Animated } from 'react-native';

const App = () => {
  const opacidad = useRef(new Animated.Value(0)).current;
  const mover = useRef(new Animated.Value(0)).current;
  const escala = useRef(new Animated.Value(1)).current;

  const animacionCompleta = () => {
    Animated.parallel([     // ← todas al mismo tiempo
      Animated.timing(opacidad, { toValue: 1, duration: 1000, useNativeDriver: true }),
      Animated.timing(mover, { toValue: 150, duration: 1000, useNativeDriver: true }),
      Animated.timing(escala, { toValue: 1.3, duration: 1000, useNativeDriver: true }),
    ]).start();
  };

  const resetear = () => {
    Animated.parallel([
      Animated.timing(opacidad, { toValue: 0, duration: 500, useNativeDriver: true }),
      Animated.timing(mover, { toValue: 0, duration: 500, useNativeDriver: true }),
      Animated.timing(escala, { toValue: 1, duration: 500, useNativeDriver: true }),
    ]).start();
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', gap: 20 }}>
      
      <Animated.View 
        style={{ 
          width: 100, 
          height: 100, 
          backgroundColor: 'orange',
          opacity: opacidad,
          transform: [
            { translateX: mover },
            { scale: escala }
          ]
        }} 
      />

      <TouchableOpacity onPress={animacionCompleta}>
        <Text style={{ backgroundColor: 'blue', color: 'white', padding: 10 }}>ANIMACIÓN COMPLETA</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={resetear}>
        <Text style={{ backgroundColor: 'gray', color: 'white', padding: 10 }}>RESETEAR</Text>
      </TouchableOpacity>

    </View>
  );
};

export default App;
''',
        'fb.animated.move.exemple':'''
import React, { useRef } from 'react';
import { View, Text, TouchableOpacity, Animated } from 'react-native';

const App = () => {
  const mover = useRef(new Animated.Value(0)).current;

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', gap: 20 }}>
      
      <Animated.View 
        style={{ 
          width: 100, 
          height: 100, 
          backgroundColor: 'green',
          transform: [{ translateX: mover }]   // ← movimiento horizontal
        }} 
      />

      <TouchableOpacity onPress={() => {
        Animated.timing(mover, {
          toValue: 200,      // se mueve 200px a la derecha
          duration: 800,
          useNativeDriver: true
        }).start();
      }}>
        <Text style={{ backgroundColor: 'blue', color: 'white', padding: 10 }}>MOVER DERECHA</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={() => {
        Animated.timing(mover, {
          toValue: 0,        // vuelve a la posición original
          duration: 800,
          useNativeDriver: true
        }).start();
      }}>
        <Text style={{ backgroundColor: 'gray', color: 'white', padding: 10 }}>REGRESAR</Text>
      </TouchableOpacity>

    </View>
  );
};

export default App;
''',
        'fb.animated.scale.exemple':'''
import React, { useRef } from 'react';
import { View, Text, TouchableOpacity, Animated } from 'react-native';

const App = () => {
  const opacidad = useRef(new Animated.Value(0)).current;

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', gap: 20 }}>
      
      <Animated.View 
        style={{ 
          width: 100, 
          height: 100, 
          backgroundColor: 'red',
          opacity: opacidad     // ← valor animado conectado
        }} 
      />

      <TouchableOpacity onPress={() => {
        Animated.timing(opacidad, {
          toValue: 1,
          duration: 1000,
          useNativeDriver: true
        }).start();
      }}>
        <Text style={{ backgroundColor: 'blue', color: 'white', padding: 10 }}>APARECER</Text>
      </TouchableOpacity>

      <TouchableOpacity onPress={() => {
        Animated.timing(opacidad, {
          toValue: 0,
          duration: 1000,
          useNativeDriver: true
        }).start();
      }}>
        <Text style={{ backgroundColor: 'gray', color: 'white', padding: 10 }}>DESAPARECER</Text>
      </TouchableOpacity>

    </View>
  );
};

export default App;
''',
        'fb.page.init':'''
import React from 'react';
import {
    Container,
    Text,
    width,
    height,
    goTo,
    backTo,

    setTheme,
    colors,
} from "../components/FletBox";

const LobbyPage = ({ navigation, route }) => {
    // const { id, params } = route.params || {};
    // navigation.navigate('Profile');
    // on_click={()=> goTo(navigation, 'Profile', {'id': 'myId'}); }
    return (
        <Container
            expand
            bgcolor=colors.background
            alignItems="center"
            justifyContent="center"
            width={ width / 2 }
            // height={ height / 2 }

            child={
                <Text
                    color=colors.text
                    textAlign='center'
                    label='hello world'
                    size={37}
                    weight='bold'
                />
            }
        />
    )
};

export default LobbyPage;
''',
        "fb.components":'''
const Component = ({params: ''}) => (
    {/* components */}
)
// export default Component;
''',
        "fb.container.init": '''
<Container 
    padding={20}
    bgcolor="blue"
    borderRadius={12}
    border={2}
    borderColor="#f4511e"
    overflow="hidden"
    justifyContent="flex-end"
    alignItems="center"
    padding={20}
    // bgImage={require('../assets/icon.png')}
    // bgImageStyle={{ 
    //   resizeMode: 'cover',
    //   opacity:1,
    //   width: 202*2,  // Más ancha que el contenedor
    //   height: 400,
    // }}
    // bgImageTransform={[ { translateX: slideValueX }, { translateY: slideValueY },
    child={
        <Text label="Hola mundo" />
    }
/>
''',

"fb.row.init": '''
<Row 
    gap={12} 
    justifyContent="center"
    // arrallax effect
    // translateX={slideValue}
    // translateY={slideValue}
    children={[
        <Text label="A" />,
        <Text label="B" />,
        <Text label="C" />
   ]} 
/>
''',

"fb.column.init": '''
<Column 
    gap={12}
    // arrallax effect
    // translateX={slideValue}
    // translateY={slideValue}
    children={[
        <Text label="1" />,
        <Text label="2" />,
        <Text label="3" />
   ]} 
/>
''',

"fb.spacer.init": '''
<Spacer />
''',

"fb.sizedbox.init": '''
<SizedBox size={50} />
''',

"fb.divider.init": '''
<Divider />
''',

"fb.safearea.init": '''
<SafeArea child={<Text label="Contenido seguro" />} />
''',

"fb.statusbar.init": '''
<StatusBar backgroundColor="#007aff" barStyle="light-content" />
''',

"fb.text.init": '''
<Text label="Welcome to FletBox" size={20} color="blue" weight="bold" />
''',

"fb.button.init": '''
<Button label="Click me" bgcolor="#007aff" on_click={() => console.log('click')} />
''',

"fb.floatingactionbutton.init": '''
<FloatingActionButton icon="add" on_click={() => console.log('FAB pressed')} />
''',

"fb.card.init": '''
<Card 
    elevation={2}
    child={
        <Container 
            padding={16}
            children={[
                <Text label="Card Title" weight="bold" />,
                <Text label="Card content" color="#666" />
            ]}
        />
    } 
/>
''',

"fb.avatar.init": '''
<Avatar source={require('./avatar.jpg')} size={50} rounded={true} border={2} borderColor="white" />
''',

"fb.image.init": '''
<Image source={require('./image.jpg')} width={200} height={200} fit="cover" />
''',

"fb.icon.init": '''
<Icon name="home" size={24} color="#007aff" />
''',

"fb.chip.init": '''
<Chip label="React" on_click={() => console.log('chip clicked')} />
''',

"fb.listtile.init": '''
<ListTile 
    leading={<Avatar label="JD" size={40} />}
    title="Juan Díaz"
    subtitle="juan@email.com"
    trailing={<Icon name="chevron-forward" size={20} />}
/>
''',

"fb.textfield.init": '''
<TextField label="Email" placeholder="user@email.com" on_change={setEmail} />
''',

"fb.checkbox.init": '''
<Checkbox label="Acepto términos y condiciones" value={accepted} on_change={setAccepted} />
''',

"fb.switch.init": '''
<Switch label="Notificaciones" value={enabled} on_change={setEnabled} />
''',

"fb.slider.init": '''
<Slider label="Brillo" value={brightness} on_change={setBrightness} showValue={true} valueFormat={(v) => `${v}%`} />
''',

"fb.rating.init": '''
<Rating value={rating} on_change={setRating} max={5} size={28} activeColor="#ffc107" />
''',

"fb.dropdown.init": '''
<Dropdown 
    label="País" 
    value={country} 
    options={[
        { label: 'España', value: 'es' },
        { label: 'México', value: 'mx' },
        { label: 'Argentina', value: 'ar' }
    ]} 
    on_change={setCountry} 
/>
''',

"fb.modalview.init": '''
<ModalView 
    visible={modalVisible} 
    on_close={() => setModalVisible(false)}
    child={
        <Card>
            <Text label="Modal Content" />
            <Button label="Close" on_click={() => setModalVisible(false)} />
        </Card>
    }
/>
''',

"fb.progressbar.init": '''
<ProgressBar value={50} label="Cargando..." showValue={true} />
''',

"fb.snackbar.init": '''
<SnackBar visible={showSnack} message="Archivo guardado" on_close={() => setShowSnack(false)} />
''',

"fb.alert.init": '''
<Alert visible={showAlert} title="Confirmar" message="¿Estás seguro?" onConfirm={handleConfirm} onCancel={() => setShowAlert(false)} />
''',

"fb.gesturedetector.init": '''
<GestureDetector on_tap={() => console.log('tap')} child={<Card child={<Text label="Tócame" />} />} />
''',

"fb.listview.init": '''
<ListView 
    data={products}
    // pagingEnabled={true}
    // horizontal={true}
    renderItem={({ item }) => (
        <Card child={<Text label={item.name} />} />
    )}
/>
''',

"fb.gridview.init": '''
<GridView 
    data={products}
    smallColumns={2}
    spacing={12}
    renderItem={({ item }) => (
        <Card child={<Text label={item.name} />} />
    )}
/>
''',
"fb.container.default": '''
<Container
    padding={16}
    bgcolor="#fff"
    borderRadius={8}
    shadow={false}
    children = {[

    ]}
/>
''',

"fb.row.default": '''
<Row 
    gap={8} 
    justifyContent="flex-start" 
    alignItems="center"
    children={[
    ]}
/>
''',

"fb.column.default": '''
<Column 
    gap={8}
    justifyContent="flex-start"
    alignItems="stretch"
    children={[

    ]}
/>
''',

"fb.spacer.default": '''
<Spacer flex={1} />
''',

"fb.sizedbox.default": '''
<SizedBox size={50} />
''',

"fb.divider.default": '''
<Divider color="#e0e0e0" height={1} marginVertical={8} />
''',

"fb.safearea.default": '''
<SafeArea 
    edges={['top', 'bottom', 'left', 'right']}
    bgcolor="#fff"
    child={<Text label="Safe Area" />}
/>
''',

"fb.statusbar.default": '''
<StatusBar backgroundColor="#fff" barStyle="dark-content" />
''',

"fb.text.default": '''
<Text label="Text" size={16} color="#000" weight="normal" />
''',

"fb.button.default": '''
<Button 
    label="Button" 
    bgcolor="#007aff" 
    color="#fff" 
    padding={12} 
    borderRadius={8} 
    on_click={()=> 
      // { navigation, route } <= add in component page
      // navigation.navigate('Profile')
      // goTo(navigation, 'Profile')
      alert('flet-Box')
    }
/>
''',
"fb.button.filled": '''
<Button 
    label="Click me" 
    bgcolor="#007aff" 
    on_click={()=> 
      // { navigation, route } <= add in component page
      // navigation.navigate('Profile')
      // goTo(navigation, 'Profile')
      alert('flet-Box')
    }
/>
''',

"fb.button.Elevated": '''
<Button
    label="Enviar"
    variant="elevated"
    bgcolor="#007aff"
    width={240}
    icon="home"
    elevation={4}
    on_click={()=> 
      // navigation.navigate('Profile')
      // goTo(navigation, 'Profile')
      alert('flet-Box')
    }
/>
''',

"fb.button.Outlined": '''
<Button
    label="Cancelar"
    variant="outlined"
    borderColor="red"
    color="red"
    on_click={()=> 
      // navigation.navigate('Profile')
      // goTo(navigation, 'Profile')
      alert('flet-Box')
    }
/>
''',

"fb.button.Text": '''
<Button
    label="Olvidé contraseña"
    variant="text"
    color="#007aff"
    on_click={()=> 
      // { navigation, route } <= add in component page
      // navigation.navigate('Profile')
      // goTo(navigation, 'Profile')
      alert('flet-Box')
    }
/>
''',

"fb.button.Icon": '''
<Button
    icon="heart"
    variant="icon"
    iconColor="red"
    on_click={()=> 
      // { navigation, route } <= add in component page
      // navigation.navigate('Profile')
      // goTo(navigation, 'Profile')
      alert('flet-Box')
    }
/>
''',

"fb.floatingactionbutton.default": '''
<FloatingActionButton 
    icon="add" 
    bgcolor="#007aff" 
    size={56} 
    on_click={()=> 
      // { navigation, route } <= add in component page
      // navigation.navigate('Profile')
      // goTo(navigation, 'Profile')
      alert('flet-Box')
    }
/>
''',

"fb.card.default": '''
<Card 
    elevation={2} 
    borderRadius={12} 
    bgcolor="#fff" 
    padding={16}
    child={<Text label="Card Content" />}
/>
''',

"fb.avatar.default": '''
<Avatar 
    size={48} 
    rounded={true} 
    bgcolor="#007aff" 
    color="#fff" 
    label="JD"
/>
''',

"fb.image.default": '''
<Image 
    source={require('./image.jpg')} 
    width={100} 
    height={100} 
    fit="cover" 
    borderRadius={8}
/>
''',

"fb.icon.default": '''
<Icon name="home" size={24} color="#000" />
''',

"fb.chip.default": '''
<Chip 
    label="Chip" 
    bgcolor="#f0f0f0" 
    color="#000" 
    on_click={() => {}}
/>
''',

"fb.listtile.default": '''
<ListTile 
    title="Title"
    subtitle="Subtitle"
    on_click={() => {}}
/>
''',

"fb.textfield.default": '''
<TextField 
    label="Label" 
    placeholder="Enter text" 
    bgcolor="#f5f5f5" 
    borderRadius={8}
    on_change={() => {}}
/>
''',

"fb.checkbox.default": '''
<Checkbox 
    label="Checkbox" 
    value={false} 
    on_change={() => {}}
/>
''',

"fb.switch.default": '''
<Switch 
    label="Switch" 
    value={false} 
    on_change={() => {}}
/>
''',

"fb.slider.default": '''
<Slider 
    label="Slider" 
    value={50} 
    min={0} 
    max={100} 
    on_change={() => {}}
/>
''',

"fb.rating.default": '''
<Rating 
    value={0} 
    max={5} 
    size={32} 
    on_change={() => {}}
/>
''',

"fb.dropdown.default": '''
<Dropdown 
    label="Dropdown" 
    value={null} 
    options={[]} 
    on_change={() => {}}
/>
''',

"fb.modalview.default": '''
<ModalView 
    visible={false} 
    on_close={() => {}}
    child={<Card child={<Text label="Modal Content" />} />}
/>
''',

"fb.progressbar.default": '''
<ProgressBar 
    value={50} 
    height={8} 
    activeColor="#007aff" 
    inactiveColor="#e0e0e0"
/>
''',

"fb.snackbar.default": '''
<SnackBar 
    visible={false} 
    message="Message" 
    duration={3000}
    on_close={() => {}}
/>
''',

"fb.alert.default": '''
<Alert 
    visible={false} 
    title="Title" 
    message="Message" 
    confirmText="OK"
    onConfirm={() => {}}
/>
''',

"fb.gesturedetector.default": '''
<GestureDetector 
    on_tap={() => {}} 
    child={<Text label="Tap me" />}
/>
''',

"fb.listview.default": '''
<ListView 
    // pagingEnabled={true}
    // horizontal={true}
    data={[]}
    renderItem={({ item }) => <Text label={item} />}
/>
''',

"fb.gridview.default": '''
<GridView 
    data={[]}
    smallColumns={2}
    spacing={8}
    renderItem={({ item }) => <Text label={item} />}
/>
''',
"fb.container.props.full": '''
// CONTAINER - Propiedades completas
direction="column"              // 'column' | 'row'
padding={8}                     // number | object
paddingLeft, paddingRight, paddingTop, paddingBottom
margin={8}                      // number | object
marginLeft, marginRight, marginTop, marginBottom
border={1}                      // number
borderLeft, borderRight, borderTop, borderBottom
borderColor="red"               // string
borderLeftColor, borderRightColor, borderTopColor, borderBottomColor
borderRadius={8}                // number
borderTopLeftRadius, borderTopRightRadius, borderBottomLeftRadius, borderBottomRightRadius
bgcolor="#007aff"               // string
bgImage={require('./bg.jpg')}   // object
bgImageStyle={{ resizeMode: 'cover' }}
expand={true}                   // boolean
justifyContent="center"         // 'flex-start' | 'center' | 'flex-end' | 'space-between'
alignItems="center"             // 'flex-start' | 'center' | 'flex-end' | 'stretch'
width={100}                     // number | string
height={100}                    // number | string
shadow={true}                   // boolean
shadowColor="#000"              // string
shadowOffsetWidth={0}           // number
shadowOffsetHeight={2}          // number
shadowOpacity={0.25}            // number
shadowRadius={3.84}             // number
elevation={5}                   // number
child={<Text />}                // ReactNode
children={[<Text />]}           // array

// bgImage={require('../assets/icon.png')}
// bgImageStyle={{ 
//   resizeMode: 'cover',
//   opacity:1,
//   width: 202*2,  // Más ancha que el contenedor
//   height: 400,
// }}
// bgImageTransform={[ { translateX: slideValueX }, { translateY: slideValueY },
''',

"fb.row.props.full": '''
// ROW - Propiedades completas (hereda de Container)
direction="row"                 // fijo
gap={8}                         // number - espacio entre hijos
justifyContent="center"         // 'flex-start' | 'center' | 'flex-end' | 'space-between'
alignItems="center"             // 'flex-start' | 'center' | 'flex-end' | 'stretch'
padding={8}                     // number | object
margin={8}                      // number | object
bgcolor="#fff"                  // string
borderRadius={8}                // number
expand={true}                   // boolean
// bgImage={require('../assets/icon.png')}
// bgImageStyle={{ 
//   resizeMode: 'cover',
//   opacity:1,
//   width: 202*2,  // Más ancha que el contenedor
//   height: 400,
// }}
// bgImageTransform={[ { translateX: slideValueX }, { translateY: slideValueY },
child={<Text />}                // ReactNode
children={[<Text />]}           // array
''',

"fb.column.props.full": '''
// COLUMN - Propiedades completas (hereda de Container)
direction="column"              // fijo
gap={8}                         // number - espacio entre hijos
justifyContent="center"         // 'flex-start' | 'center' | 'flex-end' | 'space-between'
alignItems="center"             // 'flex-start' | 'center' | 'flex-end' | 'stretch'
padding={8}                     // number | object
margin={8}                      // number | object
bgcolor="#fff"                  // string
borderRadius={8}                // number
expand={true}                   // boolean
// bgImage={require('../assets/icon.png')}
// bgImageStyle={{ 
//   resizeMode: 'cover',
//   opacity:1,
//   width: 202*2,  // Más ancha que el contenedor
//   height: 400,
// }}
// bgImageTransform={[ { translateX: slideValueX }, { translateY: slideValueY },
child={<Text />}                // ReactNode
children={[<Text />]}           // array
''',

"fb.spacer.props.full": '''
// SPACER - Propiedades completas
flex={1}                        // number - factor de crecimiento
minSize={20}                    // number - tamaño mínimo
expand={true}                   // boolean - flex: 1
''',

"fb.sizedbox.props.full": '''
// SIZEDBOX - Propiedades completas
width={100}                     // number - ancho fijo
height={50}                     // number - alto fijo
size={50}                       // number - ancho y alto (cuadrado)
expand={true}                   // boolean - flex: 1
''',

"fb.divider.props.full": '''
// DIVIDER - Propiedades completas
height={1}                      // number - altura de la línea
color="#e0e0e0"                 // string - color de la línea
marginVertical={8}              // number - margen vertical
marginHorizontal={0}            // number - margen horizontal
variant="full"                  // 'full' | 'inset' | 'middle'
inset={16}                      // number - margen izquierdo (variant='inset')
expand={true}                   // boolean - flex: 1
''',

"fb.safearea.props.full": '''
// SAFEAREA - Propiedades completas
child={<Text />}                // ReactNode - hijo único
children={[<Text />]}           // array - múltiples hijos
edges={['top', 'bottom']}       // array - 'top', 'bottom', 'left', 'right'
enabled={true}                  // boolean - habilitar safe area
bgcolor="#fff"                  // string - color de fondo
expand={true}                   // boolean - flex: 1
paddingTop={0}                  // number - padding superior manual
paddingBottom={0}               // number - padding inferior manual
paddingLeft={0}                 // number - padding izquierdo manual
paddingRight={0}                // number - padding derecho manual
''',

"fb.statusbar.props.full": '''
// STATUSBAR - Propiedades completas
barStyle="dark-content"         // 'dark-content' | 'light-content' | 'default'
backgroundColor="#fff"          // string - color de fondo (Android)
translucent={false}             // boolean - fondo transparente
hidden={false}                  // boolean - ocultar barra
animated={true}                 // boolean - animación al mostrar/ocultar
networkActivityIndicatorVisible // boolean - indicador de red (iOS)
''',

"fb.text.props.full": '''
// TEXT - Propiedades completas
label="Texto aquí"              // string - contenido
child={<Text />}                // ReactNode - hijo único
children={[<Text />]}           // array - múltiples hijos
size={16}                       // number - tamaño de fuente
fontSize={16}                   // number - tamaño de fuente
color="#007aff"                 // string - color del texto
weight="bold"                   // 'normal' | 'bold' | '100'-'900'
fontWeight="bold"               // string
align="center"                  // 'left' | 'center' | 'right' | 'justify'
textAlign="center"              // string
decoration="underline"          // 'none' | 'underline' | 'line-through'
textDecorationLine="underline"  // string
transform="uppercase"           // 'none' | 'uppercase' | 'lowercase' | 'capitalize'
textTransform="uppercase"       // string
letterSpacing={1}               // number
lineHeight={24}                 // number
italic={true}                   // boolean
fontStyle="italic"              // 'normal' | 'italic'
numberOfLines={2}               // number
ellipsizeMode="tail"            // 'head' | 'middle' | 'tail' | 'clip'
expand={true}                   // boolean
selectable={true}               // boolean
on_click={() => {}}             // function
''',

"fb.button.props.full": '''
// BUTTON - Propiedades completas
label="Botón"                   // string
child={<Text />}                // ReactNode
children={[<Text />]}           // array
icon="home"                     // string (Ionicons)
iconPosition="left"             // 'left' | 'right'
iconSize={20}                   // number
iconColor="#fff"                // string
variant="filled"                // 'filled' | 'elevated' | 'outlined' | 'text' | 'icon'
bgcolor="#007aff"               // string
color="#fff"                    // string (text color)
size={16}                       // number
weight="500"                    // string
padding={12}                    // number
paddingLeft, paddingRight, paddingTop, paddingBottom
borderRadius={23}               // number
borderColor="red"               // string (para outlined)
borderWidth={1}                 // number
elevation={4}                   // number (para elevated)
shadowColor="#000"              // string
loading={false}                 // boolean
disabled={false}                // boolean
expand={true}                   // boolean
on_click={() => {}}             // function
on_press={() => {}}             // function
on_long_press={() => {}}        // function
''',

"fb.floatingactionbutton.props.full": '''
// FLOATINGACTIONBUTTON - Propiedades completas
icon="add"                      // string
iconSize={24}                   // number
iconColor="#fff"                // string
bgcolor="#2196f3"               // string
size={56}                       // number
elevation={6}                   // number
borderRadius={28}               // number
mini={false}                    // boolean
position="bottom-right"         // 'bottom-right' | 'bottom-left' | 'bottom-center'
margin={16}                     // number
disabled={false}                // boolean
loading={false}                 // boolean
on_click={() => {}}             // function
''',

"fb.card.props.full": '''
// CARD - Propiedades completas
child={<Text />}                // ReactNode - hijo único
children={[<Text />]}           // array - múltiples hijos
elevation={2}                   // number
borderRadius={12}               // number
bgcolor="#fff"                  // string
padding={16}                    // number
paddingLeft, paddingRight, paddingTop, paddingBottom
border={1}                      // number
borderColor="#ddd"              // string
shadowColor="#000"              // string
shadowOpacity={0.1}             // number
shadowRadius={4}                // number
expand={true}                   // boolean
on_click={() => {}}             // function
''',

"fb.avatar.props.full": '''
// AVATAR - Propiedades completas
src="https://ejemplo.com/avatar.jpg"  // string
source={require('./avatar.png')}      // object
label="John Doe"                      // string
initials="JD"                         // string
size={48}                             // number
bgcolor="#ccc"                        // string
color="#fff"                          // string
rounded={true}                        // boolean
radius={8}                            // number
border={2}                            // number
borderColor="white"                   // string
online={true}                         // boolean
onlineColor="#4caf50"                 // string
onlineSize={12}                       // number
on_click={() => {}}                   // function
''',

"fb.image.props.full": '''
// IMAGE - Propiedades completas
src="https://ejemplo.com/img.jpg"  // string (URL)
source={require('./img.png')}      // object
width={100}                         // number
height={100}                        // number
radius={8}                          // number
borderRadius={8}                    // number
fit="cover"                         // 'cover' | 'contain' | 'stretch' | 'repeat' | 'center'
resizeMode="cover"                  // string
opacity={1}                         // number
bgcolor="#f0f0f0"                   // string
border={1}                          // number
borderColor="#ddd"                  // string
circular={true}                     // boolean
loading={false}                     // boolean
placeholder={<Text />}              // ReactNode
expand={true}                       // boolean
on_load={() => {}}                  // function
on_error={() => {}}                 // function
on_click={() => {}}                 // function
''',

"fb.icon.props.full": '''
// ICON - Propiedades completas
name="home"                     // string - nombre del icono (Ionicons)
size={24}                       // number - tamaño
color="#007aff"                 // string - color
opacity={1}                     // number - opacidad (0-1)
expand={true}                   // boolean - flex: 1
''',

"fb.chip.props.full": '''
// CHIP - Propiedades completas
label="Chip"                    // string
child={<Text />}                // ReactNode
children={[<Text />]}           // array
avatar={<Avatar />}             // ReactNode - avatar
icon="settings"                 // string - icono (Ionicons)
iconPosition="left"             // 'left' | 'right'
selected={false}                // boolean
disabled={false}                // boolean
closable={false}                // boolean
bgcolor="#f0f0f0"               // string
selectedBgcolor="#007aff"       // string
disabledBgcolor="#e0e0e0"       // string
color="#000"                    // string
selectedColor="#fff"            // string
disabledColor="#999"            // string
size={14}                       // number
padding={8}                     // number
paddingHorizontal={12}          // number
paddingVertical={6}             // number
borderRadius={16}               // number
expand={true}                   // boolean
on_click={() => {}}             // function
on_close={() => {}}             // function
''',

"fb.listtile.props.full": '''
// LISTTILE - Propiedades completas
title="Título"                      // string
subtitle="Subtítulo"                // string
leading={<Icon />}                  // ReactNode
trailing={<Icon />}                 // ReactNode
titleColor="#000"                   // string
titleSize={16}                      // number
titleWeight="500"                   // string
subtitleColor="#666"                // string
subtitleSize={14}                   // number
subtitleWeight="normal"             // string
padding={12}                        // number
paddingLeft, paddingRight, paddingTop, paddingBottom
height={60}                         // number
bgcolor="#fff"                      // string
borderBottom={true}                 // boolean
borderBottomColor="#e0e0e0"         // string
disabled={false}                    // boolean
selected={true}                     // boolean
selectedColor="#f0f0f0"             // string
expand={true}                       // boolean
on_click={() => {}}                 // function
on_long_press={() => {}}            // function
''',

"fb.textfield.props.full": '''
// TEXTFIELD - Propiedades completas
value={text}                        // string
label="Email"                       // string
placeholder="Escribe aquí"          // string
bgcolor="#f5f5f5"                   // string
color="#000"                        // string
size={16}                           // number
weight="normal"                     // string
padding={12}                        // number
borderRadius={8}                    // number
borderWidth={1}                     // number
borderColor="#ddd"                  // string
focusBorderColor="#007aff"          // string
width={200}                         // number | string
height={50}                         // number
expand={true}                       // boolean
multiline={false}                   // boolean
numberOfLines={1}                   // number
secureText={false}                  // boolean
keyboardType="default"              // 'default' | 'numeric' | 'email-address' | 'phone-pad'
secureTextEntry={false}             // boolean
disabled={false}                    // boolean
error={false}                       // boolean
errorText="Campo requerido"         // string
on_change={(text) => {}}            // function
on_submit={() => {}}                // function
on_focus={() => {}}                 // function
on_blur={() => {}}                  // function
''',

"fb.checkbox.props.full": '''
// CHECKBOX - Propiedades completas
value={true}                        // boolean
label="Acepto términos"             // string
disabled={false}                    // boolean
expand={true}                       // boolean
activeColor="#4caf50"               // string
inactiveColor="#ccc"                // string
size={24}                           // number
labelColor="#000"                   // string
width={200}                         // number
labelSize={16}                      // number
labelWeight="normal"                // string
on_change={(value) => {}}           // function
on_toggle={(value) => {}}           // function
''',

"fb.switch.props.full": '''
// SWITCH - Propiedades completas
value={true}                        // boolean
label="Notificaciones"              // string
disabled={false}                    // boolean
expand={true}                       // boolean
activeColor="#4caf50"               // string
inactiveColor="#2196f3"             // string
thumbColor="#fff"                   // string
width={80}                          // number
size={50}                           // number
labelColor="#000"                   // string
labelSize={16}                      // number
labelWeight="bold"                  // string
on_change={(value) => {}}           // function
on_toggle={(value) => {}}           // function
''',

"fb.slider.props.full": '''
// SLIDER - Propiedades completas
value={50}                          // number
min={0}                             // number
max={100}                           // number
step={1}                            // number
label="Brillo"                      // string
disabled={false}                    // boolean
expand={true}                       // boolean
activeColor="#4caf50"               // string
inactiveColor="#ccc"                // string
thumbColor="#fff"                   // string
width={200}                         // number
height={4}                          // number
thumbSize={20}                      // number
showValue={true}                    // boolean
valueFormat={(v) => `${v}%`}        // function
labelColor="#000"                   // string
labelSize={16}                      // number
labelWeight="normal"                // string
on_change={(value) => {}}           // function
on_change_end={(value) => {}}       // function
''',

"fb.rating.props.full": '''
// RATING - Propiedades completas
value={4}                           // number
max={5}                             // number
size={32}                           // number
spacing={4}                         // number
disabled={false}                    // boolean
activeColor="#ffc107"               // string
inactiveColor="#e4e5e9"             // string
activeIcon="star"                   // string
inactiveIcon="star-outline"         // string
label="Calificación"                // string
labelColor="#000"                   // string
labelSize={16}                      // number
labelWeight="normal"                // string
expand={true}                       // boolean
on_change={(value) => {}}           // function
''',

"fb.dropdown.props.full": '''
// DROPDOWN - Propiedades completas
value={value}                       // any
options={[{ label: 'Opción', value: 'opt' }]}  // array
label="País"                        // string
placeholder="Selecciona"            // string
disabled={false}                    // boolean
expand={true}                       // boolean
width={200}                         // number
height={50}                         // number
bgcolor="#f5f5f5"                   // string
color="#000"                        // string
borderColor="#ddd"                  // string
focusBorderColor="#007aff"          // string
borderRadius={8}                    // number
labelColor="#000"                   // string
labelSize={16}                      // number
labelWeight="normal"                // string
on_change={(value) => {}}           // function
''',

"fb.modalview.props.full": '''
// MODALVIEW - Propiedades completas
visible={true}                      // boolean
on_close={() => {}}                 // function
child={<Text />}                    // ReactNode
children={[<Text />]}               // array
transparent={true}                  // boolean
animationType="slide"               // 'slide' | 'fade' | 'none'
backgroundColor="transparent"       // string
bgcolor="red"                       // string
backdropPressable={true}            // boolean
justifyContent="center"             // string
alignItems="center"                 // string
on_show={() => {}}                  // function
on_hide={() => {}}                  // function
''',

"fb.progressbar.props.full": '''
// PROGRESSBAR - Propiedades completas
value={50}                          // number
min={0}                             // number
max={100}                           // number
label="Cargando"                    // string
showValue={true}                    // boolean
valueFormat={(v) => `${v}%`}        // function
height={8}                          // number
activeColor="#4caf50"               // string
inactiveColor="#e0e0e0"             // string
labelColor="#000"                   // string
labelSize={14}                      // number
labelWeight="normal"                // string
expand={true}                       // boolean
width={200}                         // number
''',

"fb.snackbar.props.full": '''
// SNACKBAR - Propiedades completas
visible={true}                  // boolean
message="Texto del mensaje"     // string
child={<Text />}                // ReactNode
children={[<Text />]}           // array
icon="checkmark"                // string
iconColor="#fff"                // string
actionLabel="Deshacer"          // string
actionTextColor="#4caf50"       // string
on_action={() => {}}            // function
on_close={() => {}}             // function
bgcolor="#333333"               // string
textColor="#ffffff"             // string
borderRadius={8}                // number
margin={16}                     // number
marginBottom={16}               // number
duration={4000}                 // number
position="bottom"               // 'bottom' | 'top'
''',

"fb.alert.props.full": '''
// ALERT - Propiedades completas
visible={true}                  // boolean
title="Título"                  // string
message="Mensaje"               // string
confirmText="Aceptar"           // string
cancelText="Cancelar"           // string
confirmStyle="default"          // 'default' | 'destructive' | 'cancel'
onConfirm={() => {}}            // function
onCancel={() => {}}             // function
''',

"fb.gesturedetector.props.full": '''
// GESTUREDETECTOR - Propiedades completas
child={<Text />}                    // ReactNode
children={[<Text />]}               // array
on_tap={() => {}}                   // function
on_double_tap={() => {}}            // function
on_long_press={() => {}}            // function
on_press_in={() => {}}              // function
on_press_out={() => {}}             // function
inkColor="rgba(0,0,0,0.1)"          // string
borderRadius={0}                    // number
disabled={false}                    // boolean
delayLongPress={500}                // number
''',

"fb.listview.props.full": '''
// LISTVIEW - Propiedades completas
data={[]}                           // array
// pagingEnabled={true}
horizontal={false}                  // boolean
itemWidth={150}                     // number (para horizontal)
spacing={8}                         // number
padding={spacing / 2}               // number
renderItem={({ item }) => <Text />} // function
keyExtractor={(item, index) => index.toString()}  // function
loading={false}                     // boolean
emptyText="No items"                // string
ListEmptyComponent={<Text />}       // ReactNode
showsHorizontalScrollIndicator={false}  // boolean
showsVerticalScrollIndicator={true}     // boolean
''',

"fb.gridview.props.full": '''
// GRIDVIEW - Propiedades completas
data={[]}                           // array
smallColumns={2}                    // number (< 600px)
mediumColumns={4}                   // number (600-900px)
largeColumns={6}                    // number (> 900px)
columns={2}                         // number (fijo)
spacing={8}                         // number
renderItem={({ item }) => <Text />} // function
keyExtractor={(item, index) => index.toString()}  // function
loading={false}                     // boolean
emptyText="No items"                // string
ListEmptyComponent={<Text />}       // ReactNode
showsVerticalScrollIndicator={false} // boolean
''',
"rn.view.init": '''
<View style={styles.container}>
    <Text>Contenido aquí</Text>
</View>
''',

"rn.text.init": '''
<Text style={styles.text}>Texto aquí</Text>
''',

"rn.image.init": '''
<Image 
    source={{uri: 'https://ejemplo.com/imagen.jpg'}} 
    style={{width: 100, height: 100}} 
/>
''',

"rn.scrollview.init": '''
<ScrollView>
    <Text>Contenido desplazable</Text>
    <Text>Más contenido</Text>
</ScrollView>
''',

"rn.flatlist.init": '''
<FlatList
    data={data}
    renderItem={({item}) => <Text>{item}</Text>}
    keyExtractor={(item, index) => index.toString()}
/>
''',

"rn.sectionlist.init": '''
<SectionList
    sections={sections}
    renderItem={({item}) => <Text>{item}</Text>}
    renderSectionHeader={({section}) => <Text>{section.title}</Text>}
    keyExtractor={(item, index) => index.toString()}
/>
''',

"rn.textinput.init": '''
<TextInput
    style={styles.input}
    value={value}
    onChangeText={setValue}
    placeholder="Escribe aquí"
/>
''',

"rn.switch.init": '''
<Switch
    value={value}
    onValueChange={setValue}
/>
''',

"rn.modal.init": '''
<Modal
    animationType="slide"
    transparent={true}
    visible={modalVisible}
    onRequestClose={() => setModalVisible(false)}
>
    <View style={styles.modalContainer}>
        <Text>Contenido del modal</Text>
        <Button title="Cerrar" onPress={() => setModalVisible(false)} />
    </View>
</Modal>
''',

"rn.activityindicator.init": '''
<ActivityIndicator size="large" color="#0000ff" />
''',

"rn.refreshcontrol.init": '''
<RefreshControl
    refreshing={refreshing}
    onRefresh={onRefresh}
/>
''',

"rn.keyboardavoidingview.init": '''
<KeyboardAvoidingView 
    behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    style={{flex: 1}}
>
    <TextInput placeholder="Input aquí" />
</KeyboardAvoidingView>
''',

"rn.safeareaview.init": '''
<SafeAreaView style={{flex: 1}}>
    <Text>Contenido en área segura</Text>
</SafeAreaView>
''',

"rn.pressable.init": '''
<Pressable onPress={() => console.log('pressed')}>
    <Text>Presiona aquí</Text>
</Pressable>
''',

"rn.touchableopacity.init": '''
<TouchableOpacity onPress={() => console.log('pressed')}>
    <Text>Botón</Text>
</TouchableOpacity>
''',
"rn.ext.checkbox.init": '''
import { CheckBox } from '@react-native-community/checkbox';

// 📦 Instalación:
// npm install @react-native-community/checkbox
// npx expo install @react-native-community/checkbox
// cd ios && pod install

<CheckBox
    value={isSelected}
    onValueChange={setIsSelected}
/>
''',

"rn.ext.radio.init": '''
import { RadioButton } from 'react-native-paper';

// 📦 Instalación:
// npm install react-native-paper
// npx expo install react-native-paper

<RadioButton
    value={value}
    status={checked === value ? 'checked' : 'unchecked'}
    onPress={() => setChecked(value)}
/>
''',

"rn.ext.picker.init": '''
import { Picker } from '@react-native-picker/picker';

// 📦 Instalación:
// npm install @react-native-picker/picker
// npx expo install @react-native-picker/picker
// cd ios && pod install

<Picker
    selectedValue={selectedValue}
    onValueChange={(itemValue) => setSelectedValue(itemValue)}
>
    <Picker.Item label="Opción 1" value="option1" />
    <Picker.Item label="Opción 2" value="option2" />
</Picker>
''',

"rn.ext.datetimepicker.init": '''
import DateTimePicker from '@react-native-community/datetimepicker';

// 📦 Instalación:
// npm install @react-native-community/datetimepicker
// npx expo install @react-native-community/datetimepicker
// cd ios && pod install

<DateTimePicker
    value={date}
    mode="date"
    display="default"
    onChange={(event, selectedDate) => {}}
/>
''',

"rn.ext.snackbar.init": '''
import { Snackbar } from 'react-native-paper';

// 📦 Instalación:
// npm install react-native-paper
// npx expo install react-native-paper

<Snackbar
    visible={visible}
    onDismiss={() => {}}
    duration={3000}
    action={{
        label: 'Cerrar',
        onPress: () => {},
    }}
>
    Mensaje del snackbar
</Snackbar>
''',

"rn.ext.progress.init": '''
import { ProgressBar } from 'react-native-paper';

// 📦 Instalación:
// npm install react-native-paper
// npx expo install react-native-paper

<ProgressBar progress={0.5} color="#007aff" />
''',

"rn.ext.markdown.init": '''
import Markdown from 'react-native-markdown-display';

// 📦 Instalación:
// npm install react-native-markdown-display
// npx expo install react-native-markdown-display

<Markdown>
    {`
# Título
**negrita** *cursiva*
- Lista
- Items
    `}
</Markdown>
''',
"rn.view.default": '''
<View style={{flex: 1, backgroundColor: '#fff', padding: 16}}>
    {children}
</View>
''',

"rn.text.default": '''
<Text style={{fontSize: 16, color: '#000'}}>
    {children}
</Text>
''',

"rn.image.default": '''
<Image 
    source={{uri: 'https://via.placeholder.com/100'}} 
    style={{width: 100, height: 100, borderRadius: 8}} 
/>
''',

"rn.scrollview.default": '''
<ScrollView showsVerticalScrollIndicator={false}>
    {children}
</ScrollView>
''',

"rn.flatlist.default": '''
<FlatList
    data={[]}
    renderItem={({item}) => <Text>{item}</Text>}
    keyExtractor={(item, index) => index.toString()}
    showsVerticalScrollIndicator={false}
/>
''',

"rn.sectionlist.default": '''
<SectionList
    sections={[]}
    renderItem={({item}) => <Text>{item}</Text>}
    renderSectionHeader={({section}) => <Text style={{fontWeight: 'bold'}}>{section.title}</Text>}
    keyExtractor={(item, index) => index.toString()}
/>
''',

"rn.textinput.default": '''
<TextInput
    style={{
        height: 48,
        borderWidth: 1,
        borderColor: '#ddd',
        borderRadius: 8,
        paddingHorizontal: 16,
        fontSize: 16,
        backgroundColor: '#fff'
    }}
    placeholder="Enter text"
    value={value}
    onChangeText={onChangeText}
/>
''',

"rn.switch.default": '''
<Switch
    value={false}
    onValueChange={() => {}}
    trackColor={{false: '#767577', true: '#81b0ff'}}
    thumbColor={value ? '#f5dd4b' : '#f4f3f4'}
/>
''',

"rn.modal.default": '''
<Modal
    animationType="slide"
    transparent={true}
    visible={false}
    onRequestClose={() => {}}
>
    <View style={{
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: 'rgba(0,0,0,0.5)'
    }}>
        <View style={{
            backgroundColor: '#fff',
            padding: 20,
            borderRadius: 12,
            width: '80%'
        }}>
            <Text>Modal Content</Text>
            <Button title="Close" onPress={() => {}} />
        </View>
    </View>
</Modal>
''',

"rn.activityindicator.default": '''
<ActivityIndicator size="large" color="#007aff" />
''',

"rn.refreshcontrol.default": '''
<RefreshControl
    refreshing={false}
    onRefresh={() => {}}
    colors={["#007aff"]}
/>
''',

"rn.keyboardavoidingview.default": '''
<KeyboardAvoidingView 
    behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
    style={{flex: 1}}
>
    {children}
</KeyboardAvoidingView>
''',

"rn.safeareaview.default": '''
<SafeAreaView style={{flex: 1, backgroundColor: '#fff'}}>
    {children}
</SafeAreaView>
''',

"rn.pressable.default": '''
<Pressable 
    onPress={() => {}}
    style={({pressed}) => [{opacity: pressed ? 0.7 : 1}]}
>
    <Text>Press me</Text>
</Pressable>
''',

"rn.touchableopacity.default": '''
<TouchableOpacity 
    onPress={() => {}}
    activeOpacity={0.7}
    style={{padding: 12, backgroundColor: '#007aff', borderRadius: 8}}
>
    <Text style={{color: '#fff'}}>Button</Text>
</TouchableOpacity>
''',
"rn.ext.checkbox.default": '''
<CheckBox
    value={false}
    onValueChange={() => {}}
    tintColor="#ccc"
    onTintColor="#007aff"
    onFillColor="#007aff"
/>
''',

"rn.ext.radio.default": '''
<RadioButton
    value="option1"
    status={selected === 'option1' ? 'checked' : 'unchecked'}
    onPress={() => setSelected('option1')}
/>
''',

"rn.ext.picker.default": '''
<Picker
    selectedValue={value}
    onValueChange={setValue}
    style={{height: 50, width: 200}}
>
    <Picker.Item label="Option 1" value="option1" />
    <Picker.Item label="Option 2" value="option2" />
</Picker>
''',

"rn.ext.datetimepicker.default": '''
<DateTimePicker
    value={new Date()}
    mode="date"
    display="default"
    onChange={() => {}}
/>
''',

"rn.ext.snackbar.default": '''
<Snackbar
    visible={false}
    onDismiss={() => {}}
    duration={3000}
    action={{label: 'Close', onPress: () => {}}}
>
    Message here
</Snackbar>
''',

"rn.ext.progress.default": '''
<ProgressBar progress={0.5} color="#007aff" style={{height: 8, borderRadius: 4}} />
''',

"rn.ext.markdown.default": '''
<Markdown>
    {content}
</Markdown>
''',
"rn.view.attributes": '''
// VIEW - Propiedades completas
//: [flex,position] ,[opacity,transform] ,[visible,pointerEvents]
// accessible={true}
// accessibilityLabel="View"
// collapsable={true}
// needsOffscreenAlphaCompositing={false}
// renderToHardwareTextureAndroid={false}
// shouldRasterizeIOS={false}
// elevation={4}
// hitSlop={{top:10,left:10,bottom:10,right:10}}
// nativeID="view1"
// testID="view-test"
<View style={styles.view}>
    {/* Contenido aquí */}
</View>
''',

"rn.text.attributes": '''
// TEXT - Propiedades completas
//: [fontSize,fontWeight] ,[color,textAlign] ,[numberOfLines,ellipsizeMode]
// selectable={true}
// selectionColor="#3498db"
// suppressHighlighting={false}
// allowFontScaling={true}
// maxFontSizeMultiplier={1.5}
// numberOfLines={2}
// ellipsizeMode="tail" // head, middle, tail, clip
// onPress={() => {}}
// onLongPress={() => {}}
<Text style={styles.text}>
    {/* Texto aquí */}
</Text>
''',

"rn.image.attributes": '''
// IMAGE - Propiedades completas
//: [source,resizeMode] ,[width,height] ,[borderRadius,borderWidth]
// source={{uri: 'https://ejemplo.com/imagen.jpg'}}
// source={require('./assets/imagen.png')}
// resizeMode="cover" // cover, contain, stretch, repeat, center
// fadeDuration={300}
// blurRadius={0}
// progressiveRenderingEnabled={false}
// loadingIndicatorSource={require('./assets/loader.gif')}
// onLoad={() => {}}
// onLoadStart={() => {}}
// onLoadEnd={() => {}}
// onError={() => {}}
// onProgress={() => {}}
// defaultSource={require('./assets/placeholder.png')}
<Image
    style={styles.image}
    source={{uri: 'https://ejemplo.com/imagen.jpg'}}
/>
''',

"rn.flatlist.attributes": '''
// FLATLIST - Propiedades completas
//: [data,renderItem] ,[horizontal,showsScrollIndicator] ,[numColumns,columnWrapperStyle]
// data={[]}
// renderItem={({item, index, separators}) => <Text>{item}</Text>}
// keyExtractor={(item, index) => index.toString()}
// ListHeaderComponent={<Text>Header</Text>}
// ListFooterComponent={<Text>Footer</Text>}
// ListEmptyComponent={<Text>No hay datos</Text>}
// ItemSeparatorComponent={() => <View style={{height:1,backgroundColor:'#ccc'}} />}
// horizontal={false}
// showsHorizontalScrollIndicator={true}
// showsVerticalScrollIndicator={true}
// numColumns={1}
// columnWrapperStyle={null}
// initialNumToRender={10}
// maxToRenderPerBatch={10}
// windowSize={21}
// removeClippedSubviews={true}
// getItemLayout={(data, index) => ({length: 50, offset: 50 * index, index})}
// onRefresh={() => {}}
// refreshing={false}
// onEndReached={() => {}}
// onEndReachedThreshold={0.5}
// onScroll={() => {}}
// scrollEventThrottle={50}
// pagingEnabled={false}
// snapToAlignment="start" // start, center, end
// snapToInterval={100}
<FlatList
    style={styles.list}
    data={data}
    renderItem={({item}) => (
        <Text style={styles.item}>{/* {item} */}</Text>
    )}
    keyExtractor={(item, index) => index.toString()}
/>
''',

"rn.textinput.attributes": '''
// TEXTINPUT - Propiedades completas
//: [placeholder,value] ,[keyboardType,secureTextEntry] ,[autoCapitalize,autoCorrect]
// editable={true}
// multiline={false}
// numberOfLines={1}
// maxLength={100}
// placeholderTextColor="#999"
// selectionColor="#3498db"
// cursorColor="#3498db"
// keyboardType="default" // default, email-address, numeric, phone-pad, etc.
// returnKeyType="done" // done, go, next, search, send, etc.
// secureTextEntry={false}
// autoCapitalize="none" // none, sentences, words, characters
// autoCorrect={true}
// autoComplete="off"
// textContentType="none"
// enablesReturnKeyAutomatically={true}
// clearButtonMode="never"
// clearTextOnFocus={false}
// selectTextOnFocus={false}
// spellCheck={true}
// blurOnSubmit={true}
// onFocus={() => {}}
// onBlur={() => {}}
// onSubmitEditing={() => {}}
// onKeyPress={() => {}}
<TextInput
    style={styles.input}
    value={value}
    onChangeText={setValue}
    placeholder="Escribe aquí"
/>
''',

"rn.switch.attributes": '''
// SWITCH - Propiedades completas
//: [value,onValueChange] ,[disabled,trackColor] ,[thumbColor,ios_backgroundColor]
// value={false}
// onValueChange={() => {}}
// disabled={false}
// trackColor={{false: '#767577', true: '#81b0ff'}}
// thumbColor={value ? '#f5dd4b' : '#f4f3f4'}
// ios_backgroundColor="#3e3e3e"
<Switch
    style={styles.switch}
    value={value}
    onValueChange={setValue}
/>
''',

"rn.modal.attributes": '''
// MODAL - Propiedades completas
// animationType="slide" // 'slide' | 'fade' | 'none'
// transparent={false}
// visible={false}
// onRequestClose={() => {}}
// onShow={() => {}}
// presentationStyle="fullScreen" // 'fullScreen' | 'pageSheet' | 'formSheet' | 'overFullScreen'
// supportedOrientations={['portrait', 'landscape']}
// hardwareAccelerated={true}
// statusBarTranslucent={false}
<Modal
    animationType="slide"
    transparent={true}
    visible={modalVisible}
    onRequestClose={() => {}}
>
    {/* Contenido del modal */}
</Modal>
''',

"rn.pressable.attributes": '''
// PRESSABLE - Propiedades completas
//: [onPress,onLongPress] ,[disabled,hitSlop] ,[delayLongPress,android_ripple]
// onPress={() => {}}
// onLongPress={() => {}}
// onPressIn={() => {}}
// onPressOut={() => {}}
// disabled={false}
// hitSlop={{top:10,left:10,bottom:10,right:10}}
// pressRetentionOffset={{top:10,left:10,bottom:10,right:10}}
// delayLongPress={500}
// android_ripple={{color: '#rgba(0,0,0,0.2)', borderless: false, radius: 150}}
<Pressable style={styles.pressable} onPress={() => {}}>
    <Text style={styles.pressableText}>{/* Texto aquí */}</Text>
</Pressable>
''',

"rn.touchableopacity.attributes": '''
// TOUCHABLEOPACITY - Propiedades completas
//: [activeOpacity,disabled] ,[onPress,onLongPress] ,[delayPressIn,delayPressOut]
// activeOpacity={0.7}
// disabled={false}
// hitSlop={{top:10,left:10,bottom:10,right:10}}
// pressRetentionOffset={{top:10,left:10,bottom:10,right:10}}
// onPress={() => {}}
// onLongPress={() => {}}
// onPressIn={() => {}}
// onPressOut={() => {}}
// onLayout={() => {}}
// delayPressIn={0}
// delayPressOut={0}
// delayLongPress={500}
<TouchableOpacity style={styles.button} onPress={() => {}}>
    {/* Contenido del botón */}
</TouchableOpacity>
''',
"rn.ext.checkbox.attributes": '''
// CHECKBOX - Propiedades completas (requiere @react-native-community/checkbox)
//: [value,onValueChange] ,[disabled,tintColor] ,[onFillColor,onTintColor]
// value={false}
// onValueChange={() => {}}
// disabled={false}
// tintColor="#ccc"
// onTintColor="#007aff"
// onFillColor="#007aff"
// boxType="square" // square, circle
// lineWidth={1}
// hideBox={false}
''',

"rn.ext.radio.attributes": '''
// RADIO - Propiedades completas (requiere react-native-paper)
//: [value,status] ,[onPress,disabled] ,[color,uncheckedColor]
// value="option1"
// status="checked" // 'checked' | 'unchecked'
// onPress={() => {}}
// disabled={false}
// color="#007aff"
// uncheckedColor="#999"
''',

"rn.ext.picker.attributes": '''
// PICKER - Propiedades completas (requiere @react-native-picker/picker)
//: [selectedValue,onValueChange] ,[enabled,style] ,[mode,dropdownIconColor]
// selectedValue={value}
// onValueChange={() => {}}
// enabled={true}
// mode="dialog" // 'dialog' | 'dropdown'
// dropdownIconColor="#000"
// dropdownIconRippleColor="rgba(0,0,0,0.1)"
// numberOfLines={1}
''',

"rn.ext.datetimepicker.attributes": '''
// DATETIMEPICKER - Propiedades completas (requiere @react-native-community/datetimepicker)
//: [value,onChange] ,[mode,display] ,[minimumDate,maximumDate]
// value={new Date()}
// onChange={() => {}}
// mode="date" // 'date' | 'time' | 'datetime'
// display="default" // 'default' | 'spinner' | 'calendar' | 'clock'
// minimumDate={new Date(2000, 0, 1)}
// maximumDate={new Date(2030, 11, 31)}
// minuteInterval={1}
// timeZoneOffsetInMinutes={0}
// positiveButtonLabel="OK"
// negativeButtonLabel="Cancel"
''',

"rn.ext.snackbar.attributes": '''
// SNACKBAR - Propiedades completas (requiere react-native-paper)
//: [visible,onDismiss] ,[duration,action] ,[theme,style]
// visible={false}
// onDismiss={() => {}}
// duration={3000}
// action={{label: 'Close', onPress: () => {}}}
// theme={{}}
// style={{}}
// wrapperStyle={{}}
''',

"rn.ext.progress.attributes": '''
// PROGRESSBAR - Propiedades completas (requiere react-native-paper)
//: [progress,color] ,[style,theme] ,[indeterminate,animated]
// progress={0.5} // 0 - 1
// color="#007aff"
// style={{}}
// theme={{}}
// indeterminate={false}
// animated={true}
''',

"rn.ext.markdown.attributes": '''
// MARKDOWN - Propiedades completas (requiere react-native-markdown-display)
//: [children,style] ,[markdownit,mergeStyle] ,[onLinkPress,onLinkLongPress]
// children={markdownContent}
// style={{}}
// markdownit={{}}
// mergeStyle={true}
// onLinkPress={(url) => {}}
// onLinkLongPress={(url) => {}}
// onDoubleTap={() => {}}
// onLongPress={() => {}}
// onLoad={() => {}}
// onError={(error) => {}}
''',
        'fb.animation.fullExemple': '''
import React from 'react';
import {
    Animated,
    Easing,
    SectionList, StyleSheet,
    Text,
    TouchableOpacity,
    View
} from 'react-native';

const EasingEg = () => {
    let opacity = new Animated.Value(0);

    const animate = easing => {
        opacity.setValue(0);
        Animated.timing(opacity, {
            toValue: 1,
            duration: 1200,
            easing,
        }).start();
    };

    const size = opacity.interpolate({
        inputRange: [0, 1],
        outputRange: [0, 80],
    });

    const animatedStyles = [
        styles.box,
        {
            opacity,
            width: size,
            height: size,
        },
    ];

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Press rows below to preview the Easing!</Text>
            <View style={styles.boxContainer}>
                <Animated.View style={animatedStyles} />
            </View>
            <SectionList
                style={styles.list}
                sections={SECTIONS}
                keyExtractor={item => item.title}
                renderItem={({ item }) => (
                    <TouchableOpacity onPress={() => animate(item.easing)} style={styles.listRow}>
                        <Text>{item.title}</Text>
                    </TouchableOpacity>
                )}
                renderSectionHeader={({ section: { title } }) => (
                    <Text style={styles.listHeader}>{title}</Text>
                )}
            />
        </View>
    );
};

const SECTIONS = [
    {
        title: 'Predefined animations',
        data: [
            { title: 'Bounce', easing: Easing.bounce },
            { title: 'Ease', easing: Easing.ease },
            { title: 'Elastic', easing: Easing.elastic(4) },
        ],
    },
    {
        title: 'Standard functions',
        data: [
            { title: 'Linear', easing: Easing.linear },
            { title: 'Quad', easing: Easing.quad },
            { title: 'Cubic', easing: Easing.cubic },
        ],
    },
    {
        title: 'Additional functions',
        data: [
            {
                title: 'Bezier',
                easing: Easing.bezier(0, 2, 1, -1),
            },
            { title: 'Circle', easing: Easing.circle },
            { title: 'Sin', easing: Easing.sin },
            { title: 'Exp', easing: Easing.exp },
        ],
    },
    {
        title: 'Combinations',
        data: [
            {
                title: 'In + Bounce',
                easing: Easing.in(Easing.bounce),
            },
            {
                title: 'Out + Exp',
                easing: Easing.out(Easing.exp),
            },
            {
                title: 'InOut + Elastic',
                easing: Easing.inOut(Easing.elastic(1)),
            },
        ],
    },
];

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#20232a',
    },
    title: {
        marginTop: 10,
        textAlign: 'center',
        color: '#61dafb',
    },
    boxContainer: {
        height: 160,
        alignItems: 'center',
    },
    box: {
        marginTop: 32,
        borderRadius: 4,
        backgroundColor: '#61dafb',
    },
    list: {
        backgroundColor: '#fff',
    },
    listHeader: {
        paddingHorizontal: 8,
        paddingVertical: 4,
        backgroundColor: '#f4f4f4',
        color: '#999',
        fontSize: 12,
        textTransform: 'uppercase',
    },
    listRow: {
        padding: 8,
    },
});

export default EasingEg;

''',
}

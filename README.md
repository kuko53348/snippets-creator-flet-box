# FletBox Snippets Creator

Snippet generator for **FletBox** (a JS-ish Flet-like UI framework). It builds
VSCode/Neovim-friendly snippet JSON files from Python source dictionaries,
keeping the `atributo: valor` snippet style.

## Repository layout

```
├── FletBox/                          # FletBox snippets output + sources
│   ├── FletBox.json                  # Combined snippets (attrs + widgets + modules)
│   ├── FletBox_widgets.json          # Widget snippets
│   ├── FletBox_attribute_widgets.json# Attribute/util snippets
│   ├── FletBox_modules_widgets.json  # Module templates (pages, components, helpers)
│   └── FletBox_snippets_creator/     # Source dictionaries (.py)
│       ├── FletBox_create_attributes_widgets.py
│       ├── FletBox_create_widgets.py
│       └── FletBox_create_modules_widgets.py
├── python/                           # Python (Flet) snippets: flet_*.json, python.json
├── ReactNative/                      # React Native snippets: ReactNative_*.json
├── fletbox_make_snippets.py          # Generates the FletBox JSON files
├── library_make_snippets.py          # Generates the python/ JSON files
├── react_make_snippets.py            # Generates the ReactNative/ JSON files
├── install_fletbox_snippet.sh        # Installs FletBox.json for Neovim
├── installer_snippets.sh             # Installs python.json into friendly-snippets
├── create_tutorial.py                # Helper script (FastAPI examples)
└── snippet_path/                     # FastAPI chat server + Neovim paths
```

## How it works

1. Snippets are authored as Python dictionaries, one key per snippet, value
   written in `atributo: valor` form:

   ```python
   'padding': 'padding: 16,',
   'createWidget': 'createWidget({ name: "MyWidget", ... }),'
   ```

2. The generator scripts convert each dict into snippet entries:

   ```json
   {
     "prefix": "padding",
     "description": "Make a FletBox widgets padding widget",
     "body": ["padding: 16,"]
   }
   ```

3. `FletBox.json` is the combined file: attributes are merged first and widgets
   last, so on name collisions the widget version wins (as the original export).

## Regenerate the JSON files

Run from the repository root:

```bash
python3 fletbox_make_snippets.py
```

Which rebuilds:
- `FletBox/FletBox_attribute_widgets.json`
- `FletBox/FletBox_widgets.json`
- `FletBox/FletBox_modules_widgets.json`
- `FletBox/FletBox.json` (combined)

Equivalent generators exist for the other ecosystems:
`python3 library_make_snippets.py` and `python3 react_make_snippets.py`.

## Install (Neovim)

```bash
bash install_fletbox_snippet.sh     # copies FletBox/FletBox.json → ~/.config/nvim/flet-box-snippets.json
```

## Current snippet counts

| File | Entries |
| --- | --- |
| `FletBox_widgets.json` | 248 |
| `FletBox_attribute_widgets.json` | 792 |
| `FletBox_modules_widgets.json` | 14 |
| `FletBox.json` (combined) | 1023 |

## Catálogo de snippets (keys)

Todos los `prefix` disponibles, agrupados por categoria. Estos son los keys que se pueden citar: al escribir el `prefix` en el editor se expande el snippet. Cada fuente `.py` incluye el mismo catalogo como comentario al inicio del dict.

### Atributos y utilidades
`FletBox_attribute_widgets.json`

- **ANIMATION** (1): `animation_fn`
- **ARRAY** (5): `chunk, reverse_fn, shuffle, sort, unique`
- **BORDER** (1): `border_fn`
- **CLIPBOARD** (3): `clipboard.copy, clipboard.copyWithFeedback, clipboard.read`
- **COLOR** (11): `color.alpha, color.complement, color.contrast, color.darken, color.hex, color.isDark, color.isLight, color.lighten, color.rgb, color.rgba, color_fn`
- **CREATE LIST** (9): `createList, createList.fromData, createList.groupBy, createList.paginate, createList.range, createList.repeat, createList.search, createList.sort, createWidget`
- **DELAY** (3): `delay_fn, retry, withMinDelay`
- **DEVICE** (8): `device.hasGesture, device.isDesktop, device.isMobile, device.isTablet, device.isTouch, device.onOrientationChange, device.onResize, device.orientation`
- **DIMENSIONS** (5): `dimensions.addListener, dimensions.get, dimensions.height, dimensions.removeListener, dimensions.width`
- **DICT** (5): `Dict, dict, emptyDict, fromEntries, fromJSON`
- **FILTER** (1): `filter_fn`
- **FLEX** (1): `flex_fn`
- **GRADIENT** (1): `gradient_fn`
- **GRID** (1): `grid_fn`
- **MAP LIST** (3): `mapList, range, repeat`
- **MEMO** (3): `clearMemo, memo, memoWithKey`
- **OS** (4): `os.isDesktop, os.isMobile, os.name, os.version`
- **RANDOM** (20): `random.age, random.boolean, random.choice, random.date, random.dateString, random.datetime, random.dayOfWeek, random.email, random.firstName, random.fullName, random.hexColor, random.id, random.lastName, random.month, random.number, random.rgbColor, random.string, random.time, random.timeAmPm, random.timestamp`
- **REF** (1): `ref_fn`
- **RGBA** (1): `rgba`
- **SHADOW** (1): `shadow_fn`
- **STRING** (6): `capitalize, capitalizeWords, lowerCase, reverseString, truncate, upperCase`
- **TIME** (4): `formatDate, now, relativeTime, sleep`
- **TRANSFORM** (1): `transform_fn`
- **TRANSITION** (1): `transition_fn`
- **useState** (2): `useState, useWatchState`
- **UUID** (4): `numericId, shortId, timestampId, uuid`
- **THEMES** (8): `applySystemTheme, colors, getColor, getTheme, setTheme, subscribeTheme, toggleTheme, watchSystemTheme`
- **HTTP** (5): `httpDelete, httpGet, httpPatch, httpPost, httpPut`
- **RAM STORE** (11): `clearAllRam, deleteRam, getAllRam, getAllRamKeys, getRam, getRamItemCount, hasRam, isRamAvailable, saveRam, subscribeRam, updateRam`
- **SESSION** (14): `clearAllSession, deleteSession, deleteSessionByPrefix, deleteSessionBySuffix, getAllSessionData, getAllSessionKeys, getSession, getSessionItemCount, getSessionSize, getSessionSync, hasSession, isSessionAvailable, saveSession, updateSession`
- **STORAGE** (14): `clearAllData, deleteData, deleteDataByPrefix, deleteDataBySuffix, getAllData, getAllKeys, getData, getDataSync, getItemCount, getStorageSize, hasData, isStorageAvailable, saveData, updateData`
- **getWidgetProps utils** (3): `getWidgetProp, getWidgetProps, stringifyWidgetProps`
- **markdownParser utils** (3): `markdownToWidgets, parseInlineToWidgets, parseMarkdownToWidgets`
- **mediaTime utils** (5): `formatMediaProgress, formatMediaTime, formatMediaTimeLong, getProgressPercent, percentToSeconds`
- **stopWebRefresh** (1): `stopWebRefresh`
- **syntaxHighlight** (1): `generateHighlightedHtml`
- **TextInputValidator** (13): `TextInputValidator.escapeHtml, TextInputValidator.filter, TextInputValidator.filterEmail, TextInputValidator.isEmail, TextInputValidator.isOnlyLetters, TextInputValidator.isOnlyNumbers, TextInputValidator.isSafe, TextInputValidator.limitLength, TextInputValidator.onlyAlphanumeric, TextInputValidator.onlyLetters, TextInputValidator.onlyNumbers, TextInputValidator.safeText, TextInputValidator.sanitize`
- **units** (4): `getBaseFontSize, setBaseFontSize, toPX, toREM`
- **animate.js** (8): `animate_fn, animateAsync, fadeIn, fadeInAsync, fadeOut, fadeOutAsync, pulse, pulseAsync`
- **Identificación y atributos DOM** (5): `className, id, key, ref, style`
- **Contenido y composición** (2): `child, children`
- **Espaciado (atributo: valor)** (11): `gap, margin, margin.all, margin.horizontal, margin.only, margin.vertical, padding, padding.all, padding.horizontal, padding.only, padding.vertical`
- **Dimensiones** (7): `expand, flex, height, maxHeight, maxWidth, minWidth, width`
- **Colores y fondos** (6): `backgroundColor, bgColor, color, gradient, opacity, textColor`
- **Bordes y sombras** (8): `border, borderColor, borderRadius, borderStyle, borderWidth, boxShadow, elevation, shadow`
- **Posición** (6): `bottom, left, position, right, top, zIndex`
- **Flexbox / alineación** (4): `alignItems, flexDirection, flexWrap, justifyContent`
- **Texto** (6): `align, letterSpacing, lineHeight, size, text, weight`
- **Efectos** (4): `cursor, overflow, transform, transition`
- **Eventos genéricos** (13): `onBlur, onChange, onClick, onDoublePress, onFocus, onHover, onInput, onMouseEnter, onMouseLeave, onPress, onRightClick, onScroll, onWheel`
- **Estado** (11): `checked, disabled, error, expanded, label, placeholder, readonly, required, selected, value, visible`
- **Iconos** (8): `icon, iconBottom, iconColor, iconLeft, iconPosition, iconRight, iconSize, iconTop`
- **Variantes** (3): `fullWidth, sizeVariant, variant`
- **Validación (Input)** (11): `autocomplete, customPattern, inputmode, maxLength, name, onValidated, pattern, showValidationIcon, showValidationMessage, type, validation`
- **Slider** (10): `inverted, max, min, onChanged, onChangeEnd, orientation, showValue, step, valuePrefix, valueSuffix`
- **Dropdown** (4): `clearable, optionHoverColor, options, portal`
- **Rating** (7): `activeColor, allowHalf, iconActive, iconHalf, iconInactive, inactiveColor, maxRating`
- **Progress Bar** (12): `animatedStripes, backgroundColorProgress, borderRadiusProgress, colorProgress, glow, heightProgress, indeterminate, maxProgress, progress, stripeColor, striped, valueProgress`
- **Chip** (3): `iconChip, labelChip, onDelete`
- **List Tile** (9): `description, divider, hoverColor, leftItem, rightItem, selectedBgColor, subtitle, subtitleWidget, title`
- **Card** (1): `elevationCard`
- **Avatar** (4): `alt, fit, shape, src`
- **Image** (1): `poster`
- **Button** (2): `buttonText, onLongPress`
- **Switch** (1): `onToggle`
- **Checkbox / Radio** (2): `onCheck, onSelect`
- **Snackbar** (8): `action, dismissible, duration, message, onAction, onShow, positionSnackbar, typeSnackbar`
- **Modal / BottomSheet / AlertDialog** (26): `actions, cancelText, closeOnDragDown, closeOnEsc, closeOnOverlayClick, confirmText, content, contentBgColor, footerBgColor, footerBorder, footerPadding, headerBgColor, headerBorder, headerPadding, headerTextColor, modalContentElevation, modalFooterElevation, modalHeaderElevation, onCancel, onClose, onConfirm, onOpen, overlayColor, showCloseButton, showDragHandle, variantDialog`
- **BottomSheet específico** (10): `bottomSheetActionBorderColor, bottomSheetActionPadding, bottomSheetContentPadding, bottomSheetDragHandleColor, bottomSheetDragHandleHeight, bottomSheetDragHandlePadding, bottomSheetDragHandleWidth, bottomSheetHeaderBorderColor, bottomSheetHeaderPadding, bottomSheetOverlayZIndex`
- **Accordion** (12): `animate, animationDuration, childrenAccordion, contentPadding, expandedColor, iconCollapsed, iconColorAccordion, iconExpanded, iconSizeAccordion, onToggleAccordion, titlePadding, variantAccordion`
- **Stepper** (11): `activeStep, backLabel, finishLabel, nextLabel, onFinish, onStepChange, orientationStepper, showLabelsStepper, showNavigation, steps, variantStepper`
- **Pagination** (8): `currentPage, maxButtons, onPageChange, pageSize, showFirstLast, showPrevNext, showTotal, totalItems`
- **Tree View** (23): `childrenGap, collapseIcon, defaultExpanded, expandedNodes, expandIcon, fileIcon, folderIcon, folderOpenIcon, iconSizeTree, indent, nodeGap, nodePadding, nodes, onToggleTree, selectable, selectedNodeId, showIcons, treeFolderIconColor, treeHoverBgColor, treeIconColor, treeSelectedBgColor, treeSelectedTextColor, treeTextColor`
- **Chart** (21): `areaColor, areaGradient, areaGradientColors, axisColor, barColor, candleDownColor, candleSpacing, candleUpColor, candleWidth, chartBgColor, chartPadding, data, labels, lineColor, showGrid, showLabelsChart, showValues, smooth, textColorChart, typeChart, yAxisColor`
- **QR Code** (5): `bgColorQR, errorCorrection, fgColorQR, sizeQR, valueQR`
- **Circular Bar** (34): `animateCircular, animationDurationCircular, backgroundColorCircular, colorCircular, glowCircular, glowColor, gradientCircular, innerColor, innerStrokeWidth, labelCircular, labelColor, labelSize, labelSizeCircular, lineCap, markers, maxCircular, onClickCircular, onComplete, onHoverCircular, shadowBlur, shadowColor, sizeCircular, strokeWidth, subtitleCircular, subtitleColor, subtitleSize, thumbColor, tooltipCircular, trackColor, valueCircular, valueColorCircular, valueDecimals, valueFormat, valueSizeCircular`
- **Carousel** (15): `autoPlay, buttonBgColorCarousel, buttonIconColor, buttonIconSizeCarousel, buttonSizeCarousel, dotActiveColor, dotActiveSize, dotColor, dotSize, infinite, interval, items, onIndexChange, showArrows, showDots`
- **Video / Audio** (11): `autoplay, controls, loopMedia, muted, onEnd, onLoad, onPause, onPlay, onProgress, onTimeUpdate, volume`
- **Drag & Drop** (14): `acceptGroups, cloneOnDrag, dragBorderColor, dragData, dragImage, dragOpacity, dragOverlayColor, group, onDragEnd, onDragEnter, onDragLeave, onDragOver, onDragStart, onDrop`
- **DroppBox** (12): `droppBoxActiveBgColor, droppBoxActiveBorderColor, droppBoxActiveBorderStyle, droppBoxActiveBorderWidth, droppBoxActiveShadow, droppBoxInvalidBgColor, droppBoxInvalidBorderColor, droppBoxShowFeedback, droppBoxTransitionDuration, droppBoxTransitionTiming, droppBoxValidBgColor, droppBoxValidBorderColor`
- **Tooltip** (5): `delay, offset, showArrow, tooltipPosition, tooltipText`
- **Skeleton** (8): `pulseDuration, skeletonAnimation, skeletonCount, skeletonGap, skeletonHighlightColor, skeletonShimmerColor, skeletonVariant, skeletonWaveDuration`
- **Code Viewer** (10): `code, codeBorderRadius, codeFontSize, codeMaxHeight, codeTitle, lineNumberColor, lineNumberWidth, showHeader, showLineNumbers, startingLineNumber`
- **Inspector** (3): `inspect, inspectWidget, printWidgetCode`
- **Markdown** (7): `allowDangerousHtml, blockquoteBorderColor, codeBgColor, codeColor, linkColor, markdownText, preBgColor`
- **Install Button** (2): `installText, onInstalled`
- **App Bar** (9): `actionsAppBar, backButtonRoute, centerTitle, hideOnScroll, leading, onBackPress, scrollThreshold, showBackButton, sticky`
- **Bottom Navigation** (7): `currentIndex, itemsBottomNav, onTabChange, selectedColor, showLabels, unselectedColor, useRouter`
- **Tabs** (11): `activeIndex, badges, childrenTabs, dividerColorTabs, iconPositionTabs, iconSizeTabs, onChangeTabs, showDivider, showIconTabs, tabs, variantTabs`
- **Drawer** (11): `blur, blurIntensity, closeOnEscDrawer, closeOnOverlayClickDrawer, drawerBody, drawerBorderRadius, drawerFooter, drawerHeader, drawerPosition, drawerWidth, elevationDrawer`
- **Collapsible Sidebar** (7): `borderRight, expandedSidebar, onToggleSidebar, showTooltip, tooltipDelay, widthCollapsed, widthExpanded`
- **Drawer Item** (5): `closeOnPress, disableTransform, hintColor, route, trailingIcon`
- **Scaffold** (14): `appBar, body, bottomBar, closeDrawerOnNavigate, drawer, fab, leftNavBar, leftNavBarWidth, navSideBar, navSideBarPosition, navSideBarWidth, rightNavBar, rightNavBarWidth, routes`
- **List View / Grid View** (12): `bufferSize, crossAxisCount, itemSize, ListEmptyComponent, ListFooterComponent, ListHeaderComponent, onEndReached, onEndReachedThreshold, onRefresh, renderItem, showsScrollIndicator, wrapItems`
- **Data Table** (18): `borderColorTable, bordered, borderWidthTable, cellPadding, columns, headerBgColorTable, headerCellPadding, headerFontSize, headerFontWeight, headerTextColorTable, hoverable, hoverRowBgColor, onRowClick, rowBgColor, rowFontSize, rows, rowTextColor, stripedRowBgColor`
- **Floating Action Button** (3): `elevationFAB, extended, mini`
- **Matrix Rain** (7): `chars, fadeAmount, fontSize, positionMatrix, resetProbability, speed, useDynamicColor`
- **Parallax Box** (8): `directionParallax, durationParallax, easing, maxOffset, onParallaxMove, reverse, speedParallax, typeParallax`
- **Animated Text** (4): `animations, delayBetween, orientationAnimatedText, sameTime`
- **Animated Box** (2): `fillMode, timing`
- **4. ROUTER API (funciones de navegación avanzada)** (14): `buildUrl, clearRouter, closeDrawer, destroyDrawer, getCurrentPath, getCurrentRoute, getCurrentRouteConfig, getRoute, goForward, isActive, openDrawer, replace, subscribeRouter, toggleDrawer`
- **5. CORE / PWA / HMR** (13): `createApp, getHMR, initHMR, insertAfter, insertBefore, insertBy, installPWA, isPWAInstalled, mountAll, prependBy, removePWA, replaceBy, updatePWA`
- **6. SERVICIOS (clases y HTTP)** (4): `httpRequest, RamStore, Session, Storage`
- **7. VISUAL EFFECTS (utils de animación DOM)** (7): `applyGlow, applyIndeterminate, applyPulse, applyShimmer, applyStripes, injectKeyframes, removeStripes`
- **8. MARKDOWN / SYNTAX HIGHLIGHT (utils de parser)** (5): `escapeHtml, highlightColors, parseInlineMarkdown, parseMarkdown, tokenize`
- **9. THEMES (adicional)** (2): `palettes, useTheme`
- **10. NAVIGATION / MISC UTILS** (5): `addNavigation, heightDims, printFn, stackPosition, widthDims`
- **11. PROPS EXTRA POR WIDGET (según API real del framework)** (22): `actionsGap, alignColumn, buttonTop, customValueFormatter, direction, formatterColumn, gradientAngle, marks, minHeight, onEnter, onIconPress, passwordToggle, showCancel, showMarks, textAlign, thumbSize, titleSize, titleWeight, valueColor, valuePosition, valueSize, wrap`

Total: **792**

### Widgets
`FletBox_widgets.json`

- **Container** (3): `Container.basic, Container.full, Container.normal`
- **Row** (3): `Row.basic, Row.full, Row.normal`
- **Column** (3): `Column.basic, Column.full, Column.normal`
- **Stack** (3): `Stack.basic, Stack.full, Stack.normal`
- **Expanded** (3): `Expanded.basic, Expanded.full, Expanded.normal`
- **Text** (3): `Text.basic, Text.full, Text.normal`
- **Button** (3): `Button.basic, Button.full, Button.normal`
- **Icon** (3): `Icon.basic, Icon.full, Icon.normal`
- **Image** (3): `Image.basic, Image.full, Image.normal`
- **Avatar** (3): `Avatar.basic, Avatar.full, Avatar.normal`
- **Card** (3): `Card.basic, Card.full, Card.normal`
- **Input** (3): `Input.basic, Input.full, Input.normal`
- **Dropdown** (3): `Dropdown.basic, Dropdown.full, Dropdown.normal`
- **Slider** (3): `Slider.basic, Slider.full, Slider.normal`
- **Checkbox** (3): `Checkbox.basic, Checkbox.full, Checkbox.normal`
- **Radio** (3): `Radio.basic, Radio.full, Radio.normal`
- **Switch** (3): `Switch.basic, Switch.full, Switch.normal`
- **Rating** (3): `Rating.basic, Rating.full, Rating.normal`
- **Modal** (3): `Modal.basic, Modal.full, Modal.normal`
- **BottomSheet** (3): `BottomSheet.basic, BottomSheet.full, BottomSheet.normal`
- **AlertDialog** (3): `AlertDialog.basic, AlertDialog.full, AlertDialog.normal`
- **SnackBar** (3): `SnackBar.basic, SnackBar.full, SnackBar.normal`
- **Tooltip** (3): `Tooltip.basic, Tooltip.full, Tooltip.normal`
- **Scaffold** (3): `Scaffold.basic, Scaffold.full, Scaffold.normal`
- **AdaptiveScaffold** (3): `AdaptiveScaffold.basic, AdaptiveScaffold.full, AdaptiveScaffold.normal`
- **AppBar** (3): `AppBar.basic, AppBar.full, AppBar.normal`
- **Drawer** (3): `Drawer.basic, Drawer.full, Drawer.normal`
- **BottomNavigation** (3): `BottomNavigation.basic, BottomNavigation.full, BottomNavigation.normal`
- **Tabs** (3): `Tabs.basic, Tabs.full, Tabs.normal`
- **CollapsibleSideBar** (3): `CollapsibleSideBar.basic, CollapsibleSideBar.full, CollapsibleSideBar.normal`
- **DrawerItem** (3): `DrawerItem.basic, DrawerItem.full, DrawerItem.normal`
- **Router** (19): `Router.buildUrl, Router.clearRouter, Router.closeDrawer, Router.destroyDrawer, Router.getCurrentPath, Router.getCurrentRoute, Router.getCurrentRouteConfig, Router.getRoute, Router.goBack, Router.goForward, Router.goTo, Router.init, Router.isActive, Router.openDrawer, Router.replace, Router.subscribe, Router.toggleDrawer, Router.useParams, Router.useQueryParams`
- **ListView** (3): `ListView.basic, ListView.full, ListView.normal`
- **GridView** (3): `GridView.basic, GridView.full, GridView.normal`
- **DataTable** (3): `DataTable.basic, DataTable.full, DataTable.normal`
- **Chart** (3): `Chart.basic, Chart.full, Chart.normal`
- **QRCode** (3): `QRCode.basic, QRCode.full, QRCode.normal`
- **CodeViewer** (3): `CodeViewer.basic, CodeViewer.full, CodeViewer.normal`
- **Video** (3): `Video.basic, Video.full, Video.normal`
- **Audio** (3): `Audio.basic, Audio.full, Audio.normal`
- **Carousel** (3): `Carousel.basic, Carousel.full, Carousel.normal`
- **AnimatedBox** (3): `AnimatedBox.basic, AnimatedBox.full, AnimatedBox.normal`
- **AnimatedText** (3): `AnimatedText.basic, AnimatedText.full, AnimatedText.normal`
- **MatrixRain** (3): `MatrixRain.basic, MatrixRain.full, MatrixRain.normal`
- **ParallaxBox** (3): `ParallaxBox.basic, ParallaxBox.full, ParallaxBox.normal`
- **animate** (4): `animate.custom, animate.fadeIn, animate.fadeOut, animate.pulse`
- **useState** (1): `useState`
- **httpGet** (1): `httpGet`
- **httpPost** (1): `httpPost`
- **saveData** (1): `saveData`
- **getData** (1): `getData`
- **saveSession** (1): `saveSession`
- **saveRam** (1): `saveRam`
- **colors** (1): `colors`
- **setTheme** (1): `setTheme`
- **toggleTheme** (1): `toggleTheme`
- **random** (2): `random.email, random.name`
- **delay** (1): `delay`
- **clipboard** (1): `clipboard.copy`
- **dimensions** (1): `dimensions`
- **device** (1): `device.isMobile`
- **toREM** (1): `toREM`
- **padding** (1): `padding`
- **margin** (1): `margin`
- **border** (1): `border`
- **shadow** (1): `shadow`
- **rgba** (1): `rgba`
- **gradient** (1): `gradient`
- **mapList** (1): `mapList`
- **uuid** (1): `uuid`
- **ref** (1): `ref`
- **animateAsync** (1): `animateAsync`
- **fadeInAsync** (1): `fadeInAsync`
- **fadeOutAsync** (1): `fadeOutAsync`
- **pulseAsync** (1): `pulseAsync`
- **createApp** (1): `createApp`
- **createWidget** (3): `createWidget.basic, createWidget.stateful, createWidget.withProps`
- **httpRequest** (1): `httpRequest`
- **useTheme** (1): `useTheme`
- **ThemeProvider** (3): `ThemeProvider.basic, ThemeProvider.full, ThemeProvider.normal`
- **Accordion** (3): `Accordion.basic, Accordion.full, Accordion.normal`
- **Stepper** (3): `Stepper.basic, Stepper.full, Stepper.normal`
- **Pagination** (3): `Pagination.basic, Pagination.full, Pagination.normal`
- **TreeView** (3): `TreeView.basic, TreeView.full, TreeView.normal`
- **Skeleton** (3): `Skeleton.basic, Skeleton.full, Skeleton.normal`
- **ProgressBar** (3): `ProgressBar.basic, ProgressBar.full, ProgressBar.normal`
- **CircularBar** (3): `CircularBar.basic, CircularBar.full, CircularBar.normal`
- **Divider** (3): `Divider.basic, Divider.full, Divider.normal`
- **Chip** (3): `Chip.basic, Chip.full, Chip.normal`
- **Markdown** (3): `Markdown.basic, Markdown.full, Markdown.normal`
- **Inspector** (3): `Inspector.basic, Inspector.full, Inspector.normal`
- **InstallButton** (3): `InstallButton.basic, InstallButton.full, InstallButton.normal`
- **Badge** (3): `Badge.basic, Badge.full, Badge.normal`
- **ListTile** (3): `ListTile.basic, ListTile.full, ListTile.normal`
- **FloatingActionButton** (3): `FloatingActionButton.basic, FloatingActionButton.full, FloatingActionButton.normal`
- **DraggBox** (3): `DraggBox.basic, DraggBox.full, DraggBox.normal`
- **DroppBox** (3): `DroppBox.basic, DroppBox.full, DroppBox.normal`
- **CircularChart** (3): `CircularChart.basic, CircularChart.full, CircularChart.normal`

Total: **248**

### Modules (plantillas de archivo)
`FletBox_modules_widgets.json`

- **PAGE TEMPLATES (createPage)** (2): `createPage.container, createPage.minimal`
- **SCAFFOLD TEMPLATES (createPageScaffold)** (6): `createPageScaffold.basic, createPageScaffold.bottomnav, createPageScaffold.drawer, createPageScaffold.full, createPageScaffold.router, createPageScaffold.tabs`
- **COMPONENT TEMPLATES (createComponent)** (3): `createComponent.basic, createComponent.gridview, createComponent.listview`
- **WIDGET TEMPLATES (createWidget)** (3): `createWidget.basic, createWidget.stateful, createWidget.withProps`

Total: **14**
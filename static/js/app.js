
// ===== App Install Notification & GET App Install
window.addEventListener("appinstalled", (e) => {
	fetch("/api/welcome_notification/")
	.then((res) => res.json())
	.then((data) => {
		if (Notification.permission === "granted") {
		const notify = new Notification(data[0].text_message);
		notify.addEventListener('click', function() {
			location.href = '/';
		});
		} else if (Notification.permission !== "denied") {
		Notification.requestPermission().then((permission) => {
			if (permission === "granted") {
			const notify = new Notification(data[0].text_message);
			notify.addEventListener('click', function() {
				location.href = '/';
			});
			}
		});
		}
	})
	.catch((err) => {
		console.error(err);
	});

	fetch("/api/get_app_installers/", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			os: window.navigator.userAgentData.platform || navigator.platform,
		}),
	})
	.then((response) => response.json())
	.then((data) => {
		console.log(data);
	})
	.catch((error) => {
		console.error(error);
	});
});



// ====== Splash Screen
const splashContainer = document.getElementById('splashContainer');
window.addEventListener('load', () => {
    setTimeout(() => {
        splashContainer.classList.add('splash-container-toggle');
    }, 2000);
});

// ===== Navbar
const navbarOverlayId = document.getElementById('navbarOverlay');
function navbarOverlayFunc() {
    navbarOverlayId.classList.toggle('navbar-overlay-toggle');
}

// ===== Modals
function modalFunc(id) {
    const modalId = document.getElementById(id);
    modalId.classList.toggle('modal-toggle');
    navbarOverlayId.classList.remove('navbar-overlay-toggle');
}
function modalTypeOneJobFunc(id) {
    const modalId = document.getElementById(id);
    modalId.classList.toggle('modal-toggle');
}

// ===== Collape Sidebar Toggle
function collapeSidebarToggle() {
    const sidebarId = document.getElementById('sidebar');
    const sidebarItemsId = document.getElementById('sidebarItems');
    const iconCollapeSidebarId = document.getElementById('iconCollapeSidebar');
    const textCollapeSidebarId = document.getElementById('textCollapeSidebar');
    const iconExpandSidebarId = document.getElementById('iconExpandSidebar');
    const sectionContent = document.querySelector('.section-content');
    sidebarId.classList.toggle('sidebar-toggle');
    sidebarItemsId.classList.toggle('sidebar-items-toggle');
    iconCollapeSidebarId.classList.toggle('sidebar-items-toggle');
    textCollapeSidebarId.classList.toggle('sidebar-items-toggle');
    iconExpandSidebarId.classList.toggle('sidebar-items-show');
    sectionContent.classList.toggle('sidebar-width-full');
}

// ===== Tabs
function tabSignInUpFirstFunc(tabItemFirst, tabItemSecond, tabContentFirst, tabContentSecond) {
    const tabItemFirstId = document.getElementById(tabItemFirst);
    const tabItemSecondId = document.getElementById(tabItemSecond);
    const tabContentFirstId = document.getElementById(tabContentFirst);
    const tabContentSecondId = document.getElementById(tabContentSecond);
    tabItemFirstId.classList.add('tab-active');
    tabItemSecondId.classList.remove('tab-active');
    tabContentFirstId.classList.add('tab-show');
    tabContentSecondId.classList.remove('tab-show');
}
function tabSignInUpSecondFunc(tabItemFirst, tabItemSecond, tabContentFirst, tabContentSecond) {
    const tabItemFirstId = document.getElementById(tabItemFirst);
    const tabItemSecondId = document.getElementById(tabItemSecond);
    const tabContentFirstId = document.getElementById(tabContentFirst);
    const tabContentSecondId = document.getElementById(tabContentSecond);
    tabItemFirstId.classList.remove('tab-active');
    tabItemSecondId.classList.add('tab-active');
    tabContentFirstId.classList.remove('tab-show');
    tabContentFirstId.classList.add('tab-hide');
    tabContentSecondId.classList.add('tab-show');
}

function tabContentFirstFunc(tabItemFirst, tabItemSecond, tabItemThree, tabContentFirst, tabContentSecond, tabContentThree) {
    const tabItemFirstId = document.getElementById(tabItemFirst);
    const tabItemSecondId = document.getElementById(tabItemSecond);
    const tabItemThreeId = document.getElementById(tabItemThree);
    const tabContentFirstId = document.getElementById(tabContentFirst);
    const tabContentSecondId = document.getElementById(tabContentSecond);
    const tabContentThreeId = document.getElementById(tabContentThree);
    tabItemFirstId.classList.add('tab-active');
    tabItemSecondId.classList.remove('tab-active');
    tabItemThreeId.classList.remove('tab-active');
    tabContentFirstId.classList.add('tab-show');
    tabContentSecondId.classList.remove('tab-show');
    tabContentThreeId.classList.remove('tab-show');
}
function tabContentSecondFunc(tabItemFirst, tabItemSecond, tabItemThree, tabContentFirst, tabContentSecond, tabContentThree) {
    const tabItemFirstId = document.getElementById(tabItemFirst);
    const tabItemSecondId = document.getElementById(tabItemSecond);
    const tabItemThreeId = document.getElementById(tabItemThree);
    const tabContentFirstId = document.getElementById(tabContentFirst);
    const tabContentSecondId = document.getElementById(tabContentSecond);
    const tabContentThreeId = document.getElementById(tabContentThree);
    tabItemFirstId.classList.remove('tab-active');
    tabItemThreeId.classList.remove('tab-active');
    tabItemSecondId.classList.add('tab-active');
    tabContentFirstId.classList.remove('tab-show');
    tabContentFirstId.classList.add('tab-hide');
    tabContentSecondId.classList.add('tab-show');
    tabContentThreeId.classList.remove('tab-show');
    tabContentThreeId.classList.add('tab-hide');
}
function tabContentThreeFunc(tabItemFirst, tabItemSecond, tabItemThree, tabContentFirst, tabContentSecond, tabContentThree) {
    const tabItemFirstId = document.getElementById(tabItemFirst);
    const tabItemSecondId = document.getElementById(tabItemSecond);
    const tabItemThreeId = document.getElementById(tabItemThree);
    const tabContentFirstId = document.getElementById(tabContentFirst);
    const tabContentSecondId = document.getElementById(tabContentSecond);
    const tabContentThreeId = document.getElementById(tabContentThree);
    tabItemFirstId.classList.remove('tab-active');
    tabItemSecondId.classList.remove('tab-active');
    tabItemThreeId.classList.add('tab-active');
    tabContentFirstId.classList.remove('tab-show');
    tabContentFirstId.classList.add('tab-hide');
    tabContentSecondId.classList.remove('tab-show');
    tabContentSecondId.classList.add('tab-hide');
    tabContentThreeId.classList.add('tab-show');
}

// ===== Data Share
function dataShareFunc(title, text, url) {
    const dataShare = {
        title: title,
        text: text,
        url: url
    };
    if (navigator.canShare && navigator.canShare(dataShare)) {
        navigator.share(dataShare);
    } else {
        
    }
}

// ===== Request Full Screen Modal
function requestFullScreenModalFunc(idModal, idExpandIconFullScreenModal, idCollapeIconFullScreenModal) {
    const modal = document.getElementById(idModal);
    const expandIconFullScreenModalId = document.getElementById(idExpandIconFullScreenModal);
    const collapeIconFullScreenModalId = document.getElementById(idCollapeIconFullScreenModal);
    expandIconFullScreenModalId.classList.toggle('sidebar-items-toggle');
    collapeIconFullScreenModalId.classList.toggle('sidebar-items-show');
    modal.classList.toggle('modal-full-screen-toggle');
}
function requestFullScreenModalMobileFunc(idModal, idExpandIconFullScreenModal, idCollapeIconFullScreenModal) {
    const btnZekarCounterId = document.querySelector('.btn-zekar-counter');
    const modalLineId = document.querySelector('#modalOverlayZekarCounter .modal-line');
    const modalMobile = document.getElementById(idModal);
    const expandIconFullScreenModalMobileId = document.getElementById(idExpandIconFullScreenModal);
    const collapeIconFullScreenModalMobileId = document.getElementById(idCollapeIconFullScreenModal);
    const modalOverlayZekarCounterBackwardBtnId = document.getElementById('modalOverlayZekarCounterBackwardBtn');
    expandIconFullScreenModalMobileId.classList.toggle('sidebar-items-toggle');
    collapeIconFullScreenModalMobileId.classList.toggle('sidebar-items-show');
    modalMobile.classList.toggle('modal-full-screen-mobile-toggle');
    btnZekarCounterId.classList.toggle('modal-full-screen-mobile-size-toggle');
    modalLineId.classList.toggle('sidebar-items-toggle');
    modalOverlayZekarCounterBackwardBtnId.classList.toggle('modal-full-screen-mobile-show');
}

// ===== Config Dark & Light Mode
const lightModeBtnId = document.getElementById('lightModeBtn');
const darkModeBtnId = document.getElementById('darkModeBtn');
const lightModeLogoId = document.getElementById('lightModeLogo');
const darkModeLogoId = document.getElementById('darkModeLogo');
function switchDarkLightMode() {
    darkModeBtnId.onclick = () => {
        document.body.classList.add('switch-dark-light-mode');

        darkModeLogoId.classList.add('dark-mode-logo');
        lightModeLogoId.classList.add('light-mode-logo');

        lightModeBtnId.classList.remove('tab-active');
        darkModeBtnId.classList.add('tab-active');

        localStorage.setItem('themeMode', 'dark');
    }
    lightModeBtnId.onclick = () => {
        document.body.classList.remove('switch-dark-light-mode');

        darkModeLogoId.classList.remove('dark-mode-logo');
        lightModeLogoId.classList.remove('light-mode-logo');

        darkModeBtnId.classList.remove('tab-active');
        lightModeBtnId.classList.add('tab-active');

        localStorage.setItem('themeMode', 'light');
    }

    if (localStorage.getItem('themeMode') === 'dark') {
        document.body.classList.add('switch-dark-light-mode');

        darkModeLogoId.classList.add('dark-mode-logo');
        lightModeLogoId.classList.add('light-mode-logo');

        darkModeBtnId.classList.add('tab-active');
        lightModeBtnId.classList.remove('tab-active');
    } else {
        document.body.classList.remove('switch-dark-light-mode');

        darkModeLogoId.classList.remove('dark-mode-logo');
        lightModeLogoId.classList.remove('light-mode-logo');

        lightModeBtnId.classList.add('tab-active');
        darkModeBtnId.classList.remove('tab-active');
    }
}
switchDarkLightMode();

// ===== Disable Right Click And Drag & Drop
oncontextmenu = function() {
    return false;
}
document.querySelector('img').draggable = false;
document.querySelector('a img').draggable = false;
document.querySelector('a').draggable = false;

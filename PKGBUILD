pkgname="woof-qtile-config"
pkgdesc="Woof's Qtile configuration files for Woof OS"
pkgver="1.0.0"
pkgrel=1
arch=('any')
url="https://acutewoof.github.io/qtile"
license=('MIT')
depends=('qtile')
source=('https://github.com/ACuteWoof/qtile/archive/refs/tags/v1.0.0.tar.gz')

sha256sums=("SKIP")

package() {
	cd qtile*
	cp -r ./* ~/.config/qtile
}


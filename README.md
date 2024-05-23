              <article>
                <h1>Woof OS Qtile Edition</h1>
                <div class="flex gap-4 __className_62325b">
                  <a target="_self" href="#download">Download</a
                  ><a target="_self" href="#keybinds">Keybinds</a
                  ><a target="_self" href="#configs">Configs</a
                  ><a target="_blank" href="#gallery">Gallery</a>
                </div>
                <hr />
                <img
                  alt="main image"
                  loading="lazy"
                  width="1920"
                  height="1080"
                  decoding="async"
                  data-nimg="1"
                  style="color: transparent"
                  src="/images/qtile/s4.png"
                />
                <hr />
                <section id="download">
                  <h1>Download</h1>
                  <span class="flex flex-col gap-2 md:flex-row md:gap-12"
                    ><span
                      ><h2>LeWoof Mirror</h2>
                      <a
                        target="_blank"
                        href="https://dl.os.lewoof.xyz/qtile/woofos-x86_64.iso"
                        >Latest release</a
                      ><br /><a
                        target="_blank"
                        href="https://dl.os.lewoof.xyz/qtile/"
                        >Browse downloads</a
                      ></span
                    ><span
                      ><h2>Github Mirror</h2>
                      <a
                        target="_blank"
                        href="https://github.com/woof-os/isos-qtile/releases/latest/download/woofos.iso"
                        >Latest release</a
                      ><br /><a
                        target="_blank"
                        href="https://github.com/woof-os/isos-qtile/releases"
                        >Browse downloads</a
                      ></span
                    ></span
                  >
                </section>
                <hr />
                <section id="keybinds">
                  <h1>Keybinds for Woof OS Qtile edition</h1>
                  <p>
                    Woof OS uses a tiling window manager, qtile, mainly
                    controlled using the keyboard.<br />
                    The keybinds listed here are declared in
                    <code>~/.config/qtile/config.py</code>.
                  </p>
                  By default, <kbd>[mod]</kbd> is the <kbd>Super</kbd>/<kbd
                    >mod4</kbd
                  >
                  key, which is the <kbd>⊞ Win</kbd> key on most keyboards, and
                  the <kbd>⌘ Command</kbd> key on Macs.
                  <div class="md:grid md:grid-cols-2 md:gap-12 mt-8">
                    <div>
                      <h2>Focus navigation</h2>
                      <ul>
                        <li>
                          <kbd>[mod]</kbd> <kbd>H</kbd> moves focus to the
                          <b>left</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>L</kbd> moves focus to the
                          <b>right</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>J</kbd> moves focus <b>down</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>K</kbd> moves focus <b>up</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Space</kbd> moves focus to the
                          <b>next window</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>.</kbd> moves focus to the
                          <b>next screen</b>
                        </li>
                        <p>
                          The mouse can also be used to switch focus between
                          windows by simply hovering over them.
                        </p>
                        <li>
                          <kbd>[mod]</kbd>
                          <span
                            ><span><kbd>1</kbd>/</span><span><kbd>2</kbd>/</span
                            ><span><kbd>3</kbd>/</span><span><kbd>4</kbd>/</span
                            ><span><kbd>5</kbd>/</span><span><kbd>6</kbd>/</span
                            ><span><kbd>7</kbd>/</span><span><kbd>8</kbd>/</span
                            ><span><kbd>9</kbd></span></span
                          >
                          moves focus to the workspace assigned to the ID
                        </li>
                      </ul>
                    </div>
                    <div>
                      <h2>Window arrangement</h2>
                      <ul>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Shift</kbd> <kbd>H</kbd> moves
                          focused window to the <b>left</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Shift</kbd> <kbd>L</kbd> moves
                          focused window to the <b>right</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Shift</kbd> <kbd>J</kbd> moves
                          focused window <b>down</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Shift</kbd> <kbd>K</kbd> moves
                          focused window <b>up</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Shift</kbd>
                          <kbd>Return</kbd> toggles between split and unsplit
                          sides of stack
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Tab</kbd> toggles between
                          layouts
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Shift</kbd>
                          <span
                            ><span><kbd>1</kbd>/</span><span><kbd>2</kbd>/</span
                            ><span><kbd>3</kbd>/</span><span><kbd>4</kbd>/</span
                            ><span><kbd>5</kbd>/</span><span><kbd>6</kbd>/</span
                            ><span><kbd>7</kbd>/</span><span><kbd>8</kbd>/</span
                            ><span><kbd>9</kbd></span></span
                          >
                          shifts focused window to the workspace assigned to the
                          ID
                        </li>
                      </ul>
                    </div>
                    <div>
                      <h2>Window sizing</h2>
                      <ul>
                        <li>
                          <kbd>[mod]</kbd> <kbd>CTRL</kbd> <kbd>H</kbd> grows
                          window to the <b>left</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>CTRL</kbd> <kbd>L</kbd> grows
                          window to the <b>right</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>CTRL</kbd> <kbd>J</kbd> grows
                          window <b>down</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>CTRL</kbd> <kbd>K</kbd> grows
                          window <b>up</b>
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>N</kbd> resets all window sizes
                        </li>
                      </ul>
                    </div>
                    <div>
                      <h2>Miscellaneous and launching programs</h2>
                      <ul>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Return</kbd> launches the
                          terminal (alacritty)
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>R</kbd> opens the Rofi run
                          launcher
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>P</kbd> opens the Rofi power
                          menu
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>B</kbd> launches the web browser
                          (brave)
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>C</kbd> launches the file
                          manager (vifm)
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Z</kbd> opens copied PDF URL in
                          Zathura
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Y</kbd> opens copied YouTube URL
                          in MPV (using yt-dlp)
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>F</kbd> opens the Flameshot GUI
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>S</kbd> takes a full screenshot
                          using Scrot
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>T</kbd> spawns a command using a
                          prompt
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>V</kbd> shows the active windows
                          through Rofi
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>D</kbd> sends a notification
                          including the current date and time
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>Q</kbd> kills focused window
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>CTRL</kbd> <kbd>R</kbd> restarts
                          Qtile
                        </li>
                        <li>
                          <kbd>[mod]</kbd> <kbd>CTRL</kbd> <kbd>Q</kbd> shuts
                          down Qtile
                        </li>
                      </ul>
                    </div>
                  </div>
                </section>
                <hr />
                <section id="configs">
                  <h2>Configs</h2>
                  <ul class="md:grid md:grid-cols-2 __className_62325b">
                    <li>
                      <a
                        target="_blank"
                        href="https://github.com/woof-os/iso-profile"
                        >archiso profile</a
                      >
                    </li>
                    <li>
                      <a target="_blank" href="https://github.com/woof-os/qtile"
                        >qtile</a
                      >
                    </li>
                    <li>
                      <a target="_blank" href="https://github.com/woof-os/rofi"
                        >rofi</a
                      >
                    </li>
                    <li>
                      <a target="_blank" href="https://github.com/woof-os/dunst"
                        >dunst</a
                      >
                    </li>
                    <li>
                      <a
                        target="_blank"
                        href="https://github.com/woof-os/calamares"
                        >calamares</a
                      >
                    </li>
                    <li>
                      <a
                        target="_blank"
                        href="https://github.com/woof-os/alacritty"
                        >alacritty</a
                      >
                    </li>
                    <li>
                      <a
                        target="_blank"
                        href="https://github.com/woof-os/starship"
                        >starship</a
                      >
                    </li>
                    <li>
                      <a target="_blank" href="https://github.com/woof-os/qt5"
                        >qt5</a
                      >
                    </li>
                    <li>
                      <a target="_blank" href="https://github.com/woof-os/zshrc"
                        >zsh</a
                      >
                    </li>
                    <li>
                      <a
                        target="_blank"
                        href="https://github.com/woof-os/tokyonight-gtk"
                        >gtk theme</a
                      >
                    </li>
                    <li>
                      <a
                        target="_blank"
                        href="https://github.com/woof-os/icon-config"
                        >icons</a
                      >
                    </li>
                    <li>
                      <a
                        target="_blank"
                        href="https://github.com/woof-os/wallpapers"
                        >wallpapers</a
                      >
                    </li>
                  </ul>
                </section>
                <hr />
                <section id="gallery">
                  <h1>Gallery</h1>
                  <div class="h-full w-full">
                    <div class="h-full w-full flex justify-center items-center">
                      <img
                        alt="main image"
                        loading="lazy"
                        width="1920"
                        height="1080"
                        decoding="async"
                        data-nimg="1"
                        class="h-full w-full"
                        style="color: transparent"
                        src="/images/qtile/s4.png"
                      />
                    </div>
                    <div class="w-full grid md:grid-cols-2 gap-2 mt-2">
                      <div
                        class="h-full w-full flex justify-center items-center"
                      >
                        <img
                          alt="screenshot"
                          loading="lazy"
                          width="1920"
                          height="1080"
                          decoding="async"
                          data-nimg="1"
                          style="color: transparent"
                          src="/images/qtile/s0.png"
                        />
                      </div>
                      <div
                        class="h-full w-full flex justify-center items-center"
                      >
                        <img
                          alt="screenshot"
                          loading="lazy"
                          width="1920"
                          height="1080"
                          decoding="async"
                          data-nimg="1"
                          style="color: transparent"
                          src="/images/qtile/s1.png"
                        />
                      </div>
                      <div
                        class="h-full w-full flex justify-center items-center"
                      >
                        <img
                          alt="screenshot"
                          loading="lazy"
                          width="1920"
                          height="1080"
                          decoding="async"
                          data-nimg="1"
                          style="color: transparent"
                          src="/images/qtile/s2.png"
                        />
                      </div>
                      <div
                        class="h-full w-full flex justify-center items-center"
                      >
                        <img
                          alt="screenshot"
                          loading="lazy"
                          width="1920"
                          height="1080"
                          decoding="async"
                          data-nimg="1"
                          style="color: transparent"
                          src="/images/qtile/s3.png"
                        />
                      </div>
                      <div
                        class="h-full w-full flex justify-center items-center"
                      >
                        <img
                          alt="screenshot"
                          loading="lazy"
                          width="1920"
                          height="1080"
                          decoding="async"
                          data-nimg="1"
                          style="color: transparent"
                          src="/images/qtile/s5.png"
                        />
                      </div>
                      <div
                        class="h-full w-full flex justify-center items-center"
                      >
                        <img
                          alt="screenshot"
                          loading="lazy"
                          width="1920"
                          height="1080"
                          decoding="async"
                          data-nimg="1"
                          style="color: transparent"
                          src="/images/qtile/s6.png"
                        />
                      </div>
                    </div>
                  </div>
                </section>
              </article>

from conans import ConanFile, CMake, tools


class libarmcortex_conan(ConanFile):
    name = "libarmcortex"
    version = "0.0.1"
    license = "Apache License Version 2.0"
    author = "Khalil Estell"
    url = "https://github.com/libembeddedhal/libarmcortex"
    description = "A collection of interfaces and abstractions for embedded peripherals and devices using modern C++"
    topics = ("peripherals", "hardware")
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake_find_package"
    exports_sources = "include/*", "CMakeLists.txt", "tests/*"
    no_copy_source = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if self.should_test:
            self.run("ctest -j %s --output-on-failure" % tools.cpu_count())

    def package(self):
        self.copy("*.hpp")

    def package_id(self):
        self.info.header_only()

    def requirements(self):
        self.requires("libembeddedhal/0.0.1@")
        self.requires("libxbitset/0.0.1@")

    def build_requirements(self):
        self.test_requires("boost-ext-ut/1.1.8@")

# OpenMod

[OpenMod](https://github.com/openmod/openmod) is a spiritual successor to [Rocket](Rocket.md) developed by one of Rocket's original maintainers. It has its own plugin framework, but supports compatibility with existing Rocket plugins using LDM.

## Resources

- [GitHub Repository](https://github.com/openmod/openmod)
- [Documentation](https://openmod.github.io/openmod-docs/)
- [Migrating from RocketMod to OpenMod](https://openmod.github.io/openmod-docs/user-guide/migration/rocketmod/)

## Rocket Compatibility

OpenMod offers a built-in plugin called the "OpenMod RocketMod Bridge" which supports compatibility with existing Rocket plugins without the need for workarounds or rewrites.

Caveats:

- Rocket plugins are not converted to OpenMod plugins, so they cannot be managed from OpenMod.
- Rocket has its own configuration system, permissions system, command system, etc. Another built-in plugin called "RocketMod Permission Link" can be installed for Rocket to use OpenMod's permission system instead.
- Rocket command names may conflict with OpenMod command names in which case they can be renamed, or simply prefix commands with "rocket:" instead e.g. "/rocket:god".

For a guide and further details: [Migrating from RocketMod to OpenMod](https://openmod.github.io/openmod-docs/user-guide/migration/rocketmod/)

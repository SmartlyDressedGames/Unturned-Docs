.. _doc_data_enpcholiday:

ENPCHoliday
===========

The ENPCHoliday enumerated type consists of all of the game's recognized holidays or seasonal events. You can find the duration of scheduled seasonal events in the ``Client.log`` file generated after launching the game, or in the ``HolidayUtil.cs`` source file.

The start and end times are based by the player's local time, meaning they are affected by their timezone. For Lunar New Year, the start and end dates are automatically calculated, with the duration set in the game's ``Status.json`` file.

.. note:: Some assets only support a few of the game's recognized holidays. Notably: Landscape Material Assets only support Halloween, Christmas, and April Fools' Day.

Enumerators
```````````

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Named Value
     - Description
     - Duration
   * - ``None``
     - Represents no holiday or seasonal event.
     -
   * - ``Halloween``
     - Corresponds to the `Halloween <https://en.wikipedia.org/wiki/Halloween>`_ holiday.
     - October 20, 2025 (00:00) – November 1, 2025 (12:00)
   * - ``Christmas``
     - Corresponds to the `Christmas <https://en.wikipedia.org/wiki/Christmas>`_ holiday, and other holidays within the festive season.
     - December 7, 2025 (00:00) – January 2, 2026 (12:00)
   * - ``April_Fools``
     - Corresponds to the `April Fools' Day <https://en.wikipedia.org/wiki/April_Fools%27_Day>`_ holiday.
     - April 1, 2025 (00:00) – April 1, 2025 (23:59:59)
   * - ``Valentines``
     - Corresponds to the `Valentine's Day <https://en.wikipedia.org/wiki/Valentine%27s_Day>`_ holiday.
     - February 14, 2025 (00:00) – February 14, 2025 (23:59:59)
   * - ``Pride_Month``
     - Corresponds to `Pride Month <https://en.wikipedia.org/wiki/Pride_Month>`_, a month-long observance in June.
     - June 1, 2025 (00:00) – June 30, 2025 (23:59:59)
   * - ``Lunar_New_Year``
     - Corresponds to the `Lunar New Year <https://en.wikipedia.org/wiki/Lunar_New_Year>`_ holiday.
     - Varies based on the Chinese calendar, being calculated as the day *before* Lunar New Year to 15 days *after* Lunar New Year. For example: January 28, 2025 (00:00) – February 13, 2025 (23:59:59).
   * - ``Unturned_Anniversary``
     - Corresponds to the `Lunar New Year <https://en.wikipedia.org/wiki/Lunar_New_Year>`_ holiday.
     - July 7, 2025 (00:00) – July 7, 2025 (23:59:59)
   * - ``Max``
     - Only used/implemented in the game's source code – no practical use for game assets.
     -

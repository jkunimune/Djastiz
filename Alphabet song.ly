hailyanoltulum = \relative {
	g8 e'8 e8 d16 d8 c8 c16 c8 f8 f8 e8 e8 c16 c8 d8 e16 e8 d16 c16
}
tepaltolon = \lyricmode {
	e a o i u jo la we na me ho co _ sa fe ko ta pe _
}
\score{
	<<
		\new Voice = "" {
			\time 4/4
			\clef treble
			\hailyanoltulum
		}
		\new Lyrics \lyricsto "" {
			\tepaltolon
		}
	>>
}

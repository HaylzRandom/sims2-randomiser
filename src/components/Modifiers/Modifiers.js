import './modifiers.css';

const faceModifiersArr = [
	'face outer orbit depth',
	'face earshape',
	'face ear depth difference',
	'face upper jowl width',
	'face cheek raise',
	'face ear sticking-out',
	'face ear rotation',
	'face gaunt/plump',
	'face long/short',
	'cheek size',
	'lower face width',
	'upper face width',
	'underneck up-down',
	'cheekbone fwd-back',
	'cheekbone size',
	'cheekbone up-down',
	'ear size',
];

const browModifiersArr = [
	'brow eyebrow center shift',
	'brow eyebrow head thickness',
	'brow eyebrows distance',
	'brow thickness',
	'brow up-down',
	'brow arch',
	'brow rotate',
	'brow orbit shape',
	'forehead in-out',
	'brow in-out',
];

const eyeModifiersArr = [
	'eye lower eyelid width',
	'eye lower eyelid height',
	'eye eye bag lift',
	'eye eye bag curve',
	'eye lower eyelid shift',
	'eye corners height difference',
	'eye corners distance',
	'eye upper eyelid width',
	'eye upper eyelid height',
	'eye eyelid crease lift',
	'eye eyelid crease curve',
	'eye upper eyelid shift',
	'eye lower eyelid curve',
	'eye upper eyelid lift',
	'eye upper eyelid curve',
	'eye eye squint',
	'eye eyelash curl',
	'eye size',
	'eye width',
	'outer eye down-up',
	'eye closeness',
	'eyes up-down',
	'orbit up-down',
	'eye deepness',
	'eye squint',
	'eyelash size',
	'eyes rotate',
];

const noseModifiersArr = [
	'nose nostril rotation',
	'nose nasal tip size',
	'nose nose definition',
	'nose nose root depth',
	'nose nostril height',
	'nose septum width',
	'nose size',
	'nose width',
	'nostril width',
	'nose length',
	'nose up-down',
	'nose turned up-down',
	'nose tip up-down',
	'nose tip turn',
	'bridge curve',
	'bridge in-out',
	'bridge width',
	'nose in-out',
];

const mouthModifiersArr = [
	'mouth philtrum depth',
	'mouth lower lip center height',
	"mouth cupid's bow height",
	"mouth cupid's bow width",
	'mouth lips depth difference',
	'mouth upper lip raise',
	"mouth cupid's bow shape",
	'mouth width',
	'mouth up-down',
	'mouth corner down-up',
	'lips thickness',
	'upper lip pinch',
	'lower lip pinch',
	'upper lip thickness',
	'lower lip thickness',
	'mouth corner fwd-back',
	'mouth in-out',
];

const jawModifiersArr = [
	'chin jaw definition',
	'chin chin definition',
	'chin chin cleft',
	'chin chin crease depth',
	'chin up-down',
	'chin in-out',
	'chin point',
	'jaw in-out',
	'jaw square-angled',
	'jaw width',
	'jaw taper',
];

const min = -10;
const max = 10;

const Modifiers = () => {
	const generateValue = () => {
		return Math.floor(Math.random() * (max - min + 1)) + min;
	};

	return (
		<section id='sims-modifiers'>
			<header>
				<h2>Modifiers</h2>
			</header>
			<div className='modifiers'>
				<div className='modifiers__face'>
					<h3>Face</h3>
					<ul className='modifiers__list'>
						{faceModifiersArr.map((faceVal) => (
							<li key={faceVal}>
								<p>
									<span className='title'>{faceVal}: </span>
									{generateValue()}
								</p>
							</li>
						))}
					</ul>
				</div>
				<div className='modifiers__brow'>
					<h3>Brow</h3>
					<ul className='modifiers__list'>
						{browModifiersArr.map((browVal) => (
							<li key={browVal}>
								<p>
									<span className='title'>{browVal}: </span>
									{generateValue()}
								</p>
							</li>
						))}
					</ul>
				</div>
				<div className='modifiers__eyes'>
					<h3>Eyes</h3>
					<ul className='modifiers__list'>
						{eyeModifiersArr.map((eyeVal) => (
							<li key={eyeVal}>
								<p>
									<span className='title'>{eyeVal}: </span>
									{generateValue()}
								</p>
							</li>
						))}
					</ul>
				</div>
				<div className='modifiers__nose'>
					<h3>Nose</h3>
					<ul className='modifiers__list'>
						{noseModifiersArr.map((noseVal) => (
							<li key={noseVal}>
								<p>
									<span className='title'>{noseVal}: </span>
									{generateValue()}
								</p>
							</li>
						))}
					</ul>
				</div>
				<div className='modifiers__mouth'>
					<h3>Mouth</h3>
					<ul className='modifiers__list'>
						{mouthModifiersArr.map((mouthVal) => (
							<li key={mouthVal}>
								<p>
									<span className='title'>{mouthVal}: </span>
									{generateValue()}
								</p>
							</li>
						))}
					</ul>
				</div>
				<div className='modifiers__jaw'>
					<h3>Jaw</h3>
					<ul className='modifiers__list'>
						{jawModifiersArr.map((jawVal) => (
							<li key={jawVal}>
								<p>
									<span className='title'>{jawVal}: </span>
									{generateValue()}
								</p>
							</li>
						))}
					</ul>
				</div>
			</div>
		</section>
	);
};
export default Modifiers;
